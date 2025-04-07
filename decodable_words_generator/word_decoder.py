from decodable_words_generator.utils import get_simplified_cmudict
from decodable_words_generator.phonemes import *

class WordDecoder:
    """Decodes a word into its phonetic representation based on predefined indicators.

    Attributes:
        word (str): The word to decode.
    """
    def __init__(self, word: str):
        simplified_cmudict = get_simplified_cmudict()
        """Initialize with a word and prepare processing state."""
        self.word = word.lower()
        if self.word not in simplified_cmudict:
            raise Exception("Word not found")

        self.word_phonemes = simplified_cmudict[self.word]
        self.remaining_letters = self.word
        self.remaining_sounds = self.word_phonemes
        self.letter_parts:list = []
        self.sound_parts:list = []
        self.indicators:list[Indicator] = []
        self.decodable = True
        self.decode()

    def handle_undecodable(self):
        """Mark remaining letters as undecodable and halt processing."""
        self.decodable = False
        self.letter_parts.append(self.remaining_letters)
        self.sound_parts.append(tuple(self.remaining_sounds))
        self.indicators.append(Indicator.UNDECODABLE)
        self.remaining_letters = ''
        self.remaining_sounds = []

    def process_affixes(self, affixes_dict, is_prefix=True):
        """Process prefixes and suffixes and update state accordingly."""
        affix_letter_parts = []
        affix_sound_parts = []
        affix_indicators = []

        for affix, affix_sounds in affixes_dict.items():
            affix_letters = affix.replace('-', '')
            letters_match = self.word.startswith(affix_letters) if is_prefix else self.word.endswith(affix_letters)
            for affix_sound in affix_sounds:
                sounds_match = tuple(self.word_phonemes[ : len(affix_sound)]) == affix_sound if is_prefix else tuple(self.word_phonemes[-len(affix_sound) : ]) == affix_sound
                num_sounds = len(affix_sound)
                if letters_match and sounds_match:
                    affix_letter_parts.append(affix)
                    affix_sound_parts.append(affix_sound)
                    affix_indicators.append(Indicator.LETTER_COMBO)
                    self.remaining_letters = self.remaining_letters[len(affix_letters) : ] if is_prefix else self.remaining_letters[ : -len(affix_letters)]
                    self.remaining_sounds = self.remaining_sounds[num_sounds:] if is_prefix else self.remaining_sounds[ : -num_sounds]
                    break
        return affix_letter_parts, affix_sound_parts, affix_indicators
        

    def process_single_letter_sound(self, letter, sound, indicator):
        """Process a single letter with its corresponding sound."""
        self.letter_parts.append(letter)
        self.sound_parts.append(sound)
        self.indicators.append(indicator)
        self.remaining_letters = self.remaining_letters[1:]
        self.remaining_sounds = self.remaining_sounds[len(sound) : ] if self.remaining_sounds else []

    def decode(self):
        """Main decoding function that applies all processing logic."""

        # Process prefixes and suffixes
        prefix_letter_parts, prefix_sound_parts, prefix_indicators = self.process_affixes(prefixes)
        suffix_letter_parts, suffix_sound_parts, suffix_indicators = self.process_affixes(suffixes, is_prefix = False)

        # Process through the remaining_letters:
        while len(self.remaining_letters) > 0:
            # first search through all letter combinations
            for letters, sounds in letter_combinations.items():
                for sound in sounds:
                    if self.remaining_letters.startswith(letters) and tuple(self.remaining_sounds[:len(sound)]) == sound:
                        self.letter_parts.append(letters)
                        self.sound_parts.append(sound)
                        self.indicators.append(Indicator.LETTER_COMBO)
                        self.remaining_letters = self.remaining_letters[len(letters) : ]
                        self.remaining_sounds = self.remaining_sounds[len(sound) : ]
                        break
                else:
                    # Continue searching other letter combinations if no match is found
                    continue
                # If the inner break is hit, break the outer loop as well
                break
            # Some words contain punctuation (e.g. "won't") -- skip the punctuation
            else:
                this_letter = self.remaining_letters[0]
                if not this_letter.isalpha():
                    self.remaining_letters = self.remaining_letters[1:]
                    continue

                matched = False

                # Silent E
                if (len(self.remaining_sounds) == 0 or tuple([self.remaining_sounds[0]]) not in all_vowel_sounds) and this_letter == 'e':
                    self.process_single_letter_sound(this_letter, '', Indicator.SILENT_E)
                    matched = True
                
                for indicator, sound_dict in SOUND_CATEGORIES.items():
                    for sound in sound_dict.get(this_letter, []):
                        if tuple(self.remaining_sounds[:len(sound)]) == sound:
                            self.process_single_letter_sound(this_letter, sound, indicator)
                            matched = True
                            break
                    if matched:
                        break
                    
                if not matched:
                    self.handle_undecodable()
                
        # Add back in the suffixes
        self.letter_parts = prefix_letter_parts + self.letter_parts + suffix_letter_parts
        self.sound_parts = prefix_sound_parts + self.sound_parts + suffix_sound_parts
        self.indicators = prefix_indicators + self.indicators + suffix_indicators

        self._decoded = {
            'letter_parts' : self.letter_parts, 
            'indicators' : self.indicators ,
            'sound_parts' : self.sound_parts,
            'decodable' : self.decodable
        }
    
    @property
    def decoded(self):
        return self._decoded
    
    def is_vc(self):
        """
        Determines if a given word follows the "VC" (vowel-consonant) pattern.

        A valid VC word must:
        - Contain exactly two phonetic sounds: one vowel followed by one consonant.
        - Have a valid consonant/blend ending

        Returns:
            bool: True if the word follows the VC pattern, False otherwise.
        """
        # Only assess decodable, two-letter_parts-long words.

        if not self._decoded['decodable'] or len(self._decoded['letter_parts']) != 2:
            return False

        # Generate the allowed Indicator values
        allowed_indicators = [
            [Indicator.SHORT_VOWEL, Indicator.LONG_VOWEL], 
            [Indicator.HARD_CONSONANT, Indicator.SOFT_CONSONANT, Indicator.LETTER_COMBO]
        ]
        return (
            self._decoded['indicators'][0] in allowed_indicators[0] and
            self._decoded['indicators'][1] in allowed_indicators[1]
        )
        
    def is_cvc(self):
        """
        Determines if a given word follows the "CVC" (consonant-vowel-consonant) pattern.

        A valid CVC word must:
        - Contain one consonant (or blend) followed by one vowel followed by one consonant (or blend).
        
        """
        # Only assess decodable, three-letter_parts-long words.
        if not self._decoded['decodable'] or len(self._decoded['letter_parts']) != 3:
            return False
        
        # Generate the allowed Indicator values
        allowed_indicators = [
            [Indicator.HARD_CONSONANT, Indicator.SOFT_CONSONANT, Indicator.LETTER_COMBO],
            [Indicator.SHORT_VOWEL, Indicator.LONG_VOWEL], 
            [Indicator.HARD_CONSONANT, Indicator.SOFT_CONSONANT, Indicator.LETTER_COMBO]
        ]

        # Check if the word follows the pattern
        return (
            self._decoded['indicators'][0] in allowed_indicators[0] and
            self._decoded['indicators'][1] in allowed_indicators[1] and
            self._decoded['indicators'][2] in allowed_indicators[2]
        )

    def is_cvce(self):
        """
        Determines if a given word follows the "CVCe" (consonant-vowel-consonant-e) pattern.

        A valid CVCe word must:
        - Contain one consonant (or blend) followed by one vowel followed by one consonant (or blend), followed by a silent e.
        - Only include long vowels.

        Returns:
            bool: True if the word follows the CVCe pattern, False otherwise.
        """
        # Only assess decodable, three-letter_parts-long words.
        if not self._decoded['decodable'] or len(self._decoded['letter_parts']) != 4:
            return False
        
        # Generate the allowed Indicator values
        allowed_indicators = [
            [Indicator.HARD_CONSONANT, Indicator.SOFT_CONSONANT, Indicator.LETTER_COMBO],
            [Indicator.LONG_VOWEL], 
            [Indicator.HARD_CONSONANT, Indicator.SOFT_CONSONANT, Indicator.LETTER_COMBO],
            [Indicator.SILENT_E]
        ]
        
        # Check if the word follows the pattern
        return (
            self._decoded['indicators'][0] in allowed_indicators[0] and
            self._decoded['indicators'][1] in allowed_indicators[1] and
            self._decoded['indicators'][2] in allowed_indicators[2] and
            self._decoded['indicators'][3] in allowed_indicators[3]
        )
    
    def is_cvcvc(self):
        """
        Determines if a given word follows the "CVCVC" (consonant-vowel-consonant-vowel-consonant) pattern.

        A valid CVCVC word must:
        - Contain one consonant (or blend) followed by one vowel followed by one 
            consonant (or blend), followed by another vowel, and one more consonant
            or blend.

        Returns:
            bool: True if the word follows the CVCVC pattern, False otherwise.
        """
        # Only assess decodable, three-letter_parts-long words.
        if not self._decoded['decodable'] or len(self._decoded['letter_parts']) != 5:
            return False
        
        # Generate the allowed Indicator values
        allowed_indicators = [
            [Indicator.HARD_CONSONANT, Indicator.SOFT_CONSONANT, Indicator.LETTER_COMBO],
            [Indicator.SHORT_VOWEL, Indicator.LONG_VOWEL], 
            [Indicator.HARD_CONSONANT, Indicator.SOFT_CONSONANT, Indicator.LETTER_COMBO],
            [Indicator.SHORT_VOWEL, Indicator.LONG_VOWEL], 
            [Indicator.HARD_CONSONANT, Indicator.SOFT_CONSONANT, Indicator.LETTER_COMBO],
        ]

        # Check if the word follows the pattern
        return (
            self._decoded['indicators'][0] in allowed_indicators[0] and
            self._decoded['indicators'][1] in allowed_indicators[1] and
            self._decoded['indicators'][2] in allowed_indicators[2] and
            self._decoded['indicators'][3] in allowed_indicators[3] and
            self._decoded['indicators'][4] in allowed_indicators[4]
        )