import os
import sys
import unittest
import tempfile

import yaml

sys.path.insert(1, os.path.join(sys.path[0], '../src'))  # noqa: E402
from YamlFileReader import YamlFileReader


class test_YamlFileReader(unittest.TestCase):

    def test_read(self):
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, '../data/data.yml')
        result = YamlFileReader().read(file_path)

        # Ожидаемый результат
        expected_result = {
            'Иванов Иван Иванович': [('математика', 67),
                                     ('литература', 100),
                                     ('программирование', 91)],
            'Петров Петр Петрович': [('математика', 78),
                                     ('химия', 87),
                                     ('социология', 61)]
        }
        self.assertEqual(result, expected_result)

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile('w',
                                         suffix='.yml',
                                         delete=False,
                                         encoding='utf-8') as temp_file:
            temp_file_name = temp_file.name  # Сохраняем имя файла
        with self.assertRaises(ValueError):
            YamlFileReader().read(temp_file_name)

    def test_name_read(self):
        data = [
            {
                123: {
                    'математика': 67,
                    'литература': 100,
                    'программирование': 91
                }
            }
        ]

        # Создание временного файла и запись данных
        with tempfile.NamedTemporaryFile('w+',
                                         suffix='.yml',
                                         delete=False,
                                         encoding='utf-8') as temp_file:
            yaml.dump(data,
                      temp_file,
                      default_flow_style=False,
                      allow_unicode=True)
            temp_file_name = temp_file.name  # Сохраняем имя файла

        with self.assertRaises(ValueError):
            YamlFileReader().read(temp_file_name)

    def test_desc_type(self):

        data = [
            {
                'Иванов Иван Иванович': {
                    123: 'математика',
                    'литература': 100,
                    'программирование': 91
                }
            }
        ]
        # Создание временного файла и запись данных
        with tempfile.NamedTemporaryFile('w+',
                                         suffix='.yml',
                                         delete=False,
                                         encoding='utf-8') as temp_file:
            yaml.dump(data,
                      temp_file,
                      default_flow_style=False,
                      allow_unicode=True)
            temp_file_name = temp_file.name  # Сохраняем имя файла
        with self.assertRaises(ValueError):
            YamlFileReader().read(temp_file_name)

    def test_only_name(self):

        data = [
            {
                'Иванов Иван Иванович': {
                    123: 'математика',
                    'литература': 100,
                    'программирование': 91
                }
            }
        ]
        # Создание временного файла и запись данных
        with tempfile.NamedTemporaryFile('w+',
                                         suffix='.yml',
                                         delete=False,
                                         encoding='utf-8') as temp_file:
            yaml.dump(data, temp_file,
                      default_flow_style=False,
                      allow_unicode=True)
            temp_file_name = temp_file.name  # Сохраняем имя файла
        with self.assertRaises(ValueError):
            YamlFileReader().read(temp_file_name)
