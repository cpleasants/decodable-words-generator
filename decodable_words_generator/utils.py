from decodable_words_generator.constants import TOP_N
from collections.abc import Iterable
from typing import Optional

_cmu_dict:Optional[dict] = None
_top_n:Optional[list] = None

def get_cmu_dict():
    global _cmu_dict
    if _cmu_dict is None:
        from nltk import download # type: ignore
        from nltk.corpus import cmudict # type: ignore
        download('cmudict') # will skip if already downloaded.
        _cmu_dict = cmudict.dict()
    return _cmu_dict

def get_top_n():
    global _top_n
    if _top_n is None:
        from decodable_words_generator.top_n import generate_topn
        _top_n = generate_topn(n=TOP_N)
    return _top_n

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

def get_simplified_cmudict():
    """
    Generates a simplified CMU dictionary by stripping emphasis from words in the top_n list.
    Also gets only the first pronunciation from the cmu_dict
    TODO: get all pronunciations
    """
    full_cmudict = get_cmu_dict()  # Fetch the full CMU dict
    top_n_words = get_top_n()  # Fetch the top N words
    return {
        word: strip_emphasis(full_cmudict.get(word, [None])[0]) 
        for word in top_n_words if word in full_cmudict
    }


def get_flat_list(li:Iterable):
    """Flattens an iterable that may have sub-literals into a single list."""
    output:list = []
    for value in li:
        if isinstance(value, Iterable) and not isinstance(value, str):
            output.extend(value)
        else:
            output.append(value)
    return output

def is_prefix(blend_or_digraph:str):
    return blend_or_digraph[-1] == '-'

def is_suffix(blend_or_digraph:str):
    return blend_or_digraph[0] == '-'
