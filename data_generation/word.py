import utils, word_decoder
import en_core_web_sm
import numpy as np

nlp = en_core_web_sm.load()

PARTS_OF_SPEECH = {
    "ADJ" :  "adjective",
    "ADP" :  "adposition",
    "ADV" :  "adverb",
    "AUX" :  "auxiliary",
    "CONJ" :  "conjunction",
    "CCONJ" :  "coordinating conjunction",
    "DET" :  "determiner",
    "INTJ" :  "interjection",
    "NOUN" :  "noun",
    "NUM" :  "numeral",
    "PART" :  "particle",
    "PRON" :  "pronoun",
    "PROPN" :  "proper noun",
    "PUNCT" :  "punctuation",
    "SCONJ" :  "subordinating conjunction",
    "SYM" :  "symbol",
    "VERB" :  "verb",
    "X" :  "other",
    "SPACE" :  "space"
}

PHONEME_SETS:dict = {
    "hard_consonants" : utils.hard_consonants,
    "soft_consonants" : utils.soft_consonants,
    "short_vowels" : utils.short_vowels,
    "long_vowels" : utils.long_vowels,
    # "secondary_vowel_pronunciations" : utils.secondary_vowel_pronunciations,
    "vowel_teams" : utils.vowel_teams,
    "digraphs" : utils.digraphs,
    "double_letters" : utils.double_letters,
    "prefix_digraphs" : utils.prefix_digraphs,
    "prefix_blends" : utils.prefix_blends,
    "suffix_blends" : utils.suffix_blends,
    "common_endings" : utils.common_endings
}

class Word:
    """Represents a word and its associated features.

    Attributes:
        word (str): The word itself.
        rank (int): The rank of the word based on frequency.
        part_of_speech (str): The part of speech of the word.
        decoder (WordDecoder): The WordDecoder associated with the word.
        phoneme_bitmaps (dict): A dictionary of phoneme bitmaps for the word.
        features (dict): A dictionary of features extracted from the word.
    """
    def __init__(self, word):
        self.word = word
        self.rank = self.get_rank()
        self.part_of_speech = self.get_pos()
        self.decoder = self.get_decoder()
        self.phoneme_bitmaps = self.get_phoneme_bitmaps()
        self.features = self.extract_features()

    def get_pos(self):
        """Determine (most likely) part of speech based on en_core_web_sm from spacy"""
        pos = nlp(self.word)[0].pos_ # 0th entry because it's always one word
        pos_plain = PARTS_OF_SPEECH[pos]
        return pos_plain

    def get_decoder(self):
        """Uses WordDecoder to extract the WordDecoder of the word"""
        decoder = word_decoder.WordDecoder(self.word)
        return decoder

    def get_rank(self):
        """Gets rank from the top_n """
        return utils.top_n.index(self.word)
    
    def get_phoneme_bitmaps(self):
        bitmaps = {}
        for p_set in PHONEME_SETS:
            bitmaps[p_set] = np.zeros(len(PHONEME_SETS[p_set]), dtype = np.int8)
            for i, (letter_part, phon) in enumerate(PHONEME_SETS[p_set].items()):
                if letter_part in self.decoder.letter_parts:
                    place = self.decoder.letter_parts.index(letter_part)
                    if self.decoder.sound_parts[place] in phon:
                        bitmaps[p_set][i] = 1
        return bitmaps

    def extract_features(self):
        features = {
            'word' : self.word,
            'rank' : self.rank,
            'part_of_speech' : self.part_of_speech,
            'is_vc' : self.decoder.is_vc(),
            'is_cvc' : self.decoder.is_cvc(),
            'is_cvce' : self.decoder.is_cvce(),
            'is_cvcvc' : self.decoder.is_cvcvc(),
            'has_silent_e' : word_decoder.Indicator.SILENT_E in self.decoder.indicators
        }
        
        features.update(self.decoder.decoded)
        features.update(self.phoneme_bitmaps)

        return features
