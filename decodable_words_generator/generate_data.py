from decodable_words_generator import utils, word
from decodable_words_generator.constants import *
import pandas as pd

def generate_data():
    """Generates features for all words in the simplified CMU dictionary."""
    all_features = []
    for wrd in utils.simplified_cmudict:
        w = word.Word(wrd)
        all_features.append(w.features)
    return all_features

def wrangle_data(features_list):
    """Wrangles the features list into a DataFrame and filters based on decodability and rank.

    Args:
        features_list (list): A list of features to be converted into a DataFrame.

    Returns:
        pd.DataFrame: A filtered DataFrame containing only relevant features.
    """
    df = pd.DataFrame(features_list)
    decodable_mask = (df.decodable) & (df['rank'] <= MAX_DECODABLE_RANK)
    undecodable_mask = (~df.decodable) & (df['rank'] <= MAX_UNDECODABLE_RANK)
    df_included = df[decodable_mask | undecodable_mask]
    return df_included

def save_data(df:pd.DataFrame, filename):
    df.to_pickle(f"processed/{filename}")


def main():
    features = generate_data()
    df = wrangle_data(features)
    save_data(df, f"words-{MAX_DECODABLE_RANK}-decodable-{MAX_UNDECODABLE_RANK}-undecodable.pickle")

if __name__ == '__main__':
    main()