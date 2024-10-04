import os
import sys
import unittest
sys.path.insert(1, os.path.join(sys.path[0], '../src'))
from QuartRating import QuartRating  # noqa: E402


class test_QuartRating(unittest.TestCase):

    def test_quart_single(self):
        ratings = {
            "Иванов": 70,
        }
        with self.assertRaises(ValueError) as context:
            quart_rating = QuartRating(ratings).quart_students()


    def test_quart_data(self):
        ratings = {
            "Иванов": 70,
            "Петров": 80,
            "Сидоров": 81,
            "Максимов": 20,
            "Артемов": 100,
            "Фадеев": 60,
        }
        quart_rating = QuartRating(ratings).quart_students()
        expected = {
            'Сидоров': 81,
            'Артемов': 100
        }
        self.assertEqual(quart_rating.items(), expected.items())
