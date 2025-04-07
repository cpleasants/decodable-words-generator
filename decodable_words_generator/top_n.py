import gzip   # To read .gz compressed files
from nltk import FreqDist # type: ignore

def tokenize_clean_text(fname):
    """
    Reads a gzip-compressed text file, tokenizes the words,
    converts them to lowercase, and filters out tokens that
    don't start and end with alphabetic characters. Note that
    the data used in this project is highly cleaned, such as
    punctuation already having been separated from the words.

    Args:
        fname (str): Path to the .gz file

    Returns:
        list: A list of cleaned, lowercase words
    """
    words = []
    with gzip.open(fname, 'rt') as f:
        for line in f.readlines():
            # Split line into words, lowercase them, and filter
            words += [
                wrd.lower()
                for wrd in line.split(' ')
                if len(wrd) > 0 and wrd[0].isalpha() and wrd[-1].isalpha()
            ]
    return words

def tokenize_files(files_list):
    """
    Tokenizes and cleans words from multiple compressed files.

    Args:
        files_list (list): List of .gz file paths

    Returns:
        list: Combined list of cleaned words from all files
    """
    words = []
    for f in files_list:
        words.extend(tokenize_clean_text(f))
    return words

def topn(words_list, n=10000):
    """
    Returns the top-N most frequent words as a list.

    Args:
        words_list (list): A list of words
        n (int): Number of top words to include

    Returns:
        set: Set of top-N frequent words
    """
    fdist = FreqDist(words_list)
    return [x[0] for x in fdist.most_common(n)]

def generate_topn(n=10000, files=None):
    """
    High-level function to generate a top-N word set from a list of files.

    Args:
        n (int): Number of top words to return
        files (list, optional): List of .gz file paths. Defaults to preset list.

    Returns:
        set: Set of top-N frequent words
    """
    if files is None:
        files = ['data/aochildes.train.gz', 'data/cbt.train.gz', 'data/children_stories.train.gz']

    words = tokenize_files(files)
    return topn(words, n)
