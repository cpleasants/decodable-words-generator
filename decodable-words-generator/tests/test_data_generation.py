import unittest
from word import Word
from word_decoder import WordDecoder
from utils import strip_emphasis
from generate_data import generate_data, wrangle_data
import pandas as pd

class TestWord(unittest.TestCase):
    def test_initialization(self):
        word = Word('example')
        self.assertEqual(word.word, 'example')
        self.assertIsInstance(word.rank, int)

    def test_get_rank(self):
        word = Word('example')
        rank = word.get_rank()
        self.assertIsInstance(rank, int)

    def test_get_pos(self):
        word = Word('example')
        pos = word.get_pos()  # Assuming the method exists
        self.assertIsInstance(pos, str)
        # Add more assertions based on expected part of speech

    def test_get_phoneme_bitmaps(self):
        word = Word('example')
        bitmaps = word.get_phoneme_bitmaps()  # Assuming the method exists
        self.assertIsInstance(bitmaps, list)
        # Add assertions to check the content of bitmaps

class TestWordDecoder(unittest.TestCase):
    def test_initialization(self):
        decoder = WordDecoder('example')
        self.assertEqual(decoder.word, 'example')

    def test_decoding(self):
        decoder = WordDecoder('example')
        phonetic = decoder.decode()  # Assuming decode method exists
        self.assertIsInstance(phonetic, str)

    def test_decode_method(self):
        decoder = WordDecoder('example')
        phonetic = decoder.decode()  # Assuming decode method exists
        self.assertIsInstance(phonetic, str)
        # Add assertions based on expected phonetic output

class TestUtils(unittest.TestCase):
    def test_strip_emphasis(self):
        phonemes = ['UW1', 'AH0', 'D', 'M', 'P', 'L', 'IY']
        stripped = strip_emphasis(phonemes)
        self.assertEqual(stripped, ['UW', 'AH', 'D', 'M', 'P', 'L', 'IY'])

    def test_strip_emphasis_empty(self):
        phonemes = []
        stripped = strip_emphasis(phonemes)
        self.assertEqual(stripped, [])

    def test_strip_emphasis_no_emphasis(self):
        phonemes = ['D', 'M', 'P', 'L', 'IY']
        stripped = strip_emphasis(phonemes)
        self.assertEqual(stripped, phonemes)

class TestGenerateData(unittest.TestCase):
    def test_generate_data(self):
        features = generate_data()
        self.assertIsInstance(features, list)

    def test_wrangle_data(self):
        features = generate_data()
        df = wrangle_data(features)
        self.assertIsInstance(df, pd.DataFrame)
    
    def test_generate_data_empty(self):
        # Mock the simplified_cmudict to be empty
        utils.simplified_cmudict = []
        features = generate_data()
        self.assertEqual(features, [])

    def test_wrangle_data_invalid(self):
        with self.assertRaises(ValueError):  # Adjust based on expected error
            wrangle_data(None)  # Pass invalid data to see if it raises an error

class TestWordFeatures(unittest.TestCase):
    def test_word_features_example(self):
        word = Word('example')
        expected_features = {
            'rank': 1,  # Replace with the expected rank for 'example'
            'part_of_speech': 'noun',  # Replace with the expected part of speech
            'phoneme_bitmaps': [ ... ],  # Replace with expected phoneme bitmaps
            'decodable': True,  # Replace with expected decodable status
            # Add more expected features based on your implementation
        }
        self.assertEqual(word.rank, expected_features['rank'])
        self.assertEqual(word.part_of_speech, expected_features['part_of_speech'])
        self.assertEqual(word.phoneme_bitmaps, expected_features['phoneme_bitmaps'])
        self.assertEqual(word.decodable, expected_features['decodable'])

    def test_word_features_another_example(self):
        word = Word('test')
        expected_features = {
            'rank': 2,  # Replace with the expected rank for 'test'
            'part_of_speech': 'verb',  # Replace with the expected part of speech
            'phoneme_bitmaps': [ ... ],  # Replace with expected phoneme bitmaps
            'decodable': True,  # Replace with expected decodable status
        }
        self.assertEqual(word.rank, expected_features['rank'])
        self.assertEqual(word.part_of_speech, expected_features['part_of_speech'])
        self.assertEqual(word.phoneme_bitmaps, expected_features['phoneme_bitmaps'])
        self.assertEqual(word.decodable, expected_features['decodable'])

if __name__ == '__main__':
    unittest.main()