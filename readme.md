# Decodable Words Generator

## Description

A Python library for generating a DataFrame with linguistic features of words to assess their decodability.

## Installation

To install the `decodable-words-generator`, you can use the following command:

```bash
pip install -e .
```

This will install the package along with its dependencies. The required dependencies are:

- nltk
- wordfreq
- spacy (with en_core_web_sm)

Make sure you have Python version 3.6 or higher.

Usage
Change the constants in `constants.py` to what you would like the generator to use, then run `python generate_data.py`.

To use modules of this package, you can import them, for example:

```python
from decodable_words_generator import word

# Example
w = word.Word("decode")
w.features # the features associated with the word "decode"
```

# Goals

1. Create an API
2. Create a front end form
    2(a) use js/react after python implementation
3. 


First letters:
 - m, s, r, t, n, p, o, c, a, d
 - g, f, b, k, i, l, h, w
 - e, v, j, u, y, z, x, q




First digraphs
 - -ck
 - sh
 - th
 - ch
 - wh
 - qu


# VC, CVC words

blends 
L-blends: bl-, cl-, fl-, gl-, pl-, sl-
R-blends: br-, cr-, dr-, fr-, gr-, pr-, tr-
S-blends: sc-, shr-, sk-, sm-, sn-, sp-, squ-, st-, sw-

ay, ow, oy


-lp, -st, -ct, -pt, -sk, -lk, -lf, -xt, -ft, -nd, -mp, -st, -lt, -nch

-ing, -ang, -ong, -ung, -ank, -ink, -onk, -unk

-ild, -old, -ind, -olt, -ost

Open & Closed syllable types
when the syllable ends in a vowel, the door is open (long sound)

Words with the VC/CV pattern
nap/kin muf/fin ban/dit inst/ruct


Suffix -ed
Teach your students that the suffix -ed is used to show the past tense of verbs. It can represent /t/, /d/, or /id/.

CVCE (Magic e) words




Less common digraphs, trigraphs, and silent letters
wr-, kn-, ph-, gh-, gn-, -mb, -tch, -dge



Common vowel teams
ee, ea, (eat), ai, ay, oa, ow (grow), oe, igh, y (dry), oo (zoo), oo (good)

Spelling with -k, -ke, and -ck


SYLLABLES?


# add in word frequency


https://www.readingrockets.org/classroom/scope-and-sequence

https://www.readingrockets.org/sites/default/files/2023-10/NJTSS%20Phonics%20Scope%20and%20Sequence.pdf



#TODO: Sight words: top X not in Y


TODO: # Open/closed syllable types (ends in vowel)
