from constants import *
from phonemes import *
import nltk
from nltk.corpus import cmudict
from wordfreq import top_n_list
from collections.abc import Iterable


# Download -- will skip if already downloaded.
nltk.download('cmudict')

# Create a simplified version of the CMU dictionary, with only TOP_N words, and emphasis stripped.

def strip_emphasis(word_phonemes: list):
    """Strips the emphasis in the list of phonemes (e.g. 'UW1' -> 'UW').

    Args:
        word_phonemes (list): A list of phonemes with potential emphasis.

    Returns:
        list: A list of phonemes with emphasis stripped.
    """
    stripped = []
    for phoneme in word_phonemes:
        stripped.append(''.join(c for c in phoneme if c.isalpha()))
    return stripped

top_n = top_n_list('en', MAX_DECODABLE_RANK)
full_cmudict = cmudict.dict()

simplified_cmudict = {
    word : strip_emphasis(full_cmudict[word][0]) for word in top_n if word in full_cmudict
}


# Create some useful combinations of the phonemes

def get_flat_list(li:Iterable):
    """Flattens an iterable that may have sub-literals into a single list."""
    output:list = []
    for value in li:
        if isinstance(value, Iterable) and not isinstance(value, str):
            output.extend(value)
        else:
            output.append(value)
    return output

short_vowel_sounds = get_flat_list(short_vowels.values())
long_vowels_sounds = get_flat_list(long_vowels.values())
vowel_team_sounds = get_flat_list(vowel_teams.values())
all_vowel_sounds = set(short_vowel_sounds + long_vowels_sounds + vowel_team_sounds)

letter_combinations = vowel_teams | digraphs | double_letters


def is_prefix(blend_or_digraph:str):
    return blend_or_digraph[-1] == '-'

def is_suffix(blend_or_digraph:str):
    return blend_or_digraph[0] == '-'

prefixes:dict = dict()
suffixes:dict = dict()

for d in [vowel_teams, digraphs, prefix_blends, suffix_blends, common_endings, prefix_digraphs]:
    prefixes = prefixes | {k: v for k, v in d.items() if is_prefix(k)}
    suffixes = suffixes | {k: v for k, v in d.items() if is_suffix(k)}
