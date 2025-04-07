from decodable_words_generator import utils, word
from decodable_words_generator.constants import *
import pandas as pd

def generate_data():
    """Generates features for all words in the simplified CMU dictionary."""
    all_features = []
    simplified_cmudict = utils.get_simplified_cmudict()
    for wrd in simplified_cmudict:
        w = word.Word(wrd)
        all_features.append(w.features)
    return all_features

def save_data(df:pd.DataFrame, filename):
    df.to_pickle(f"processed/{filename}")


def main():
    features = generate_data()
    df = pd.DataFrame(features)
    save_data(df, f"{TOP_N}-words.pickle")

if __name__ == '__main__':
    main()