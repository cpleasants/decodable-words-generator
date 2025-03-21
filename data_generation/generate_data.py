from data_generation import utils, word
from data_generation.constants import *
import pandas as pd
import json
import numpy as np

def generate_data():
    all_features = []
    for wrd in utils.simplified_cmudict:
        w = word.Word(wrd)
        all_features.append(w.features)
    return all_features

def wrangle_data(features_list):
    df = pd.DataFrame(features_list)
    decodable_mask = (df.decodable) & (df['rank'] <= MAX_DECODABLE_RANK)
    undecodable_mask = (~df.decodable) | (df['rank'] <= MAX_UNDECODABLE_RANK)
    df_included = df[decodable_mask & undecodable_mask]
    return df_included