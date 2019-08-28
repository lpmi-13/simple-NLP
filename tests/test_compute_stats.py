import unittest
from simple_nlp.calculate_stats import calculate_type_token_ratio
from simple_nlp.utils import find_total_unique_words
from simple_nlp.utils import find_total_words
from simple_nlp.utils import find_top_ten_words
DATA_SOURCE = './data/sample.txt'

class ComputeAllStats(unittest.TestCase):

    def test_total_words(self):
        with open(DATA_SOURCE, 'r') as input_file:
            data = input_file.read()
        expected_total_words = 85
        result = find_total_words(data)
        self.assertEqual(expected_total_words, result)

    def test_total_unique_words(self):
        with open(DATA_SOURCE, 'r') as input_file:
            data = input_file.read()
        expected_total_unique_words = 61
        result = find_total_unique_words(data)
        self.assertEqual(expected_total_unique_words, result)        

    def test_top_ten_words(self):
        with open(DATA_SOURCE, 'r') as input_file:
            data = input_file.read()
        expected_top_ten_words = {'the': 9, 'in': 4, 'that': 2, 'examples': 2, 'they': 2, 'use': 2, 'will': 2, 'to': 2, 'a': 2, 'of': 2}
        result = find_top_ten_words(data)
        self.assertEqual(expected_top_ten_words, result)

    def test_calculate_type_token_ratio(self):
        with open(DATA_SOURCE, 'r') as input_file:
            data = input_file.read()
        expected_type_token_ratio = 0.72
        result = calculate_type_token_ratio(data)
        self.assertEqual(expected_type_token_ratio, result)
