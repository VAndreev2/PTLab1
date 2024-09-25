import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from CalcInfo import CalcInfo

class test_YamlFileReader(unittest.TestCase):

    def test_number_negative(self):
        expected_result = {
            'Иванов Иван Иванович': [('математика', -100),
                                     ('литература', 100),
                                     ('программирование', 91)],
            'Петров Петр Петрович': [('математика', 78),
                                     ('химия', 87),
                                     ('социология', 61)]
        }

        with self.assertRaises(ValueError):
            CalcInfo(expected_result).calc_high_rating()

    def test_number_biggest(self):
        expected_result = {
            'Иванов Иван Иванович': [('математика', 1000),
                                     ('литература', 100),
                                     ('программирование', 91)],
            'Петров Петр Петрович': [('математика', 78),
                                     ('химия', 87),
                                     ('социология', 61)]
        }

        with self.assertRaises(ValueError):
            CalcInfo(expected_result).calc_high_rating()
