# import word_decoder
# from data_generation import word
import pandas as pd
import joblib
import numpy as np

import sys
sys.path.append('../../data_generation')
import word 

def load_data():
    return joblib.load("../../data_generation/processed/words-20000-decodable-2000-undecodable.pickle")

def get_phoneme_bitmaps(p_set:str, letter_list:list):
    # TODO: consider abstracting this in order to be used with Word's implementation
    bitmap = np.zeros(len(word.PHONEME_SETS[p_set]), dtype = np.int8)
    for i, letter_part in enumerate(word.PHONEME_SETS[p_set]):
        if letter_part in letter_list:
            bitmap[i] = 1
    return bitmap

def parse_input(input_data:str):
    # parsed = json.loads(input_data)
    input_data.update({p_set : get_phoneme_bitmaps(p_set, input_data[p_set]) for p_set in word.PHONEME_SETS})
    return input_data

def filt(row: pd.Series, parsed_input: dict) -> bool:
    """
    Filters dictionary_df rows based on whether all letters/features in parsed_input
    are sufficient to construct the word in the given row.
    """
    # Check if each component in parsed_input is sufficient
    checks = [
        (parsed_input["hard_consonants"] >= row["hard_consonants"]).all(),
        (parsed_input["soft_consonants"] >= row["soft_consonants"]).all(),
        (parsed_input["long_vowels"] >= row["long_vowels"]).all(),
        (parsed_input["vowel_teams"] >= row["vowel_teams"]).all(),
        (parsed_input["digraphs"] >= row["digraphs"]).all(),
        (parsed_input["double_letters"] >= row["double_letters"]).all(),
        (parsed_input["prefix_digraphs"] >= row["prefix_digraphs"]).all(),
        (parsed_input["prefix_blends"] >= row["prefix_blends"]).all(),
        (parsed_input["suffix_blends"] >= row["suffix_blends"]).all(),
        (parsed_input["common_endings"] >= row["common_endings"]).all(),
    ]

    if parsed_input["decodable_only"]:
        checks.append(row["decodable"])
    
    if not parsed_input["allow_silent_e"]:
        checks.append(not row["has_silent_e"])

    if not parsed_input["allow_vc"]:
        checks.append(not row["is_vc"])

    if not parsed_input["allow_cvc"]:
        checks.append(not row["is_cvc"])

    if not parsed_input["allow_cvce"]:
        checks.append(not row["is_cvce"])

    if not parsed_input["allow_cvcvc"]:
        checks.append(not row["is_cvcvc"])

    # Check for decodability constraint
    if parsed_input["decodable_only"]:
        checks.append(row["decodable"])

    return all(checks)

def filter_words(dictionary_df:pd.DataFrame, parsed_input:dict):
    filtered_df = dictionary_df[dictionary_df.apply(lambda row: filt(row, parsed_input), axis=1)]
    return filtered_df
