from data_generation import utils, word
import pandas as pd
import json
import numpy as np

def generate_words(input_data:str):
    criteria = parse_input(input_data)
    all_features = []
    for wrd in utils.simplified_cmudict:
        w = word.Word(wrd)
        all_features.append(w.features)
    df = pd.DataFrame(all_features)

def get_phoneme_bitmaps(p_set:str, letter_list:list):
    # TODO: consider abstracting this in order to be used with Word's implementation
    bitmap = np.zeros(len(word.PHONEME_SETS[p_set]), dtype = np.int8)
    for i, letter_part in enumerate(p_set):
        if letter_part in letter_list:
            bitmap[i] = 1
    return bitmap

def parse_input(input_data:str):
    parsed = json.loads(input_data)
    parsed.update({p_set : get_phoneme_bitmaps(p_set, parsed[p_set]) for p_set in word.PHONEME_SETS})
    return parsed
