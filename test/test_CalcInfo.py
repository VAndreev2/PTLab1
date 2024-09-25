import os
import sys
import unittest
sys.path.insert(1, os.path.join(sys.path[0], '../src'))
from CalcInfo import CalcInfo  # noqa: E402

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
