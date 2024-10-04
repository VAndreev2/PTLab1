import os
import sys
import unittest
import tempfile

sys.path.insert(1, os.path.join(sys.path[0], '../src'))  # noqa: E402
from JsonFileReader import JsonFileReader


class test_JsonFileReader(unittest.TestCase):

    def test_read(self):
        result = JsonFileReader().read("../data/data.json")

        # Ожидаемый результат
        expected_result = {
            'Иванов Иван Иванович': [('математика', 67), ('литература', 100), ('программирование', 91)],
            'Петров Петр Петрович': [('математика', 78), ('химия', 87), ('социология', 61)]
        }
        self.assertEqual(result, expected_result)

    def test_desc_type(self):

        data = {
                'Иванов Иван Иванович': {
                    'математика': '123',
                    'литература': 100,
                    'программирование': 91
                }
        }
        # Создание временного файла и запись данных
        with tempfile.NamedTemporaryFile('w+',
                                         suffix='.json',
                                         delete=False,
                                         encoding='utf-8') as temp_file:
            json.dump(data, temp_file, ensure_ascii=False, indent=4)
            temp_file_name = temp_file.name  # Сохраняем имя файла
        try:
            with self.assertRaises(ValueError):
                JsonFileReader().read(temp_file_name)
        finally:
            # Удаление временного файла вручную после использования
            if os.path.exists(temp_file_name):
                os.remove(temp_file_name)

    def test_number_negative(self):

        data = {
                "Иванов Иван Иванович": {
                    'математика': 67,
                    'литература': -100,
                    'программирование': 91
                }
        }

        # Создание временного файла и запись данных
        with tempfile.NamedTemporaryFile('w+',
                                         suffix='.json',
                                         delete=False,
                                         encoding='utf-8') as temp_file:
            json.dump(data, temp_file, ensure_ascii=False, indent=4)
            temp_file_name = temp_file.name  # Сохраняем имя файла
        try:
            with self.assertRaises(ValueError):
                JsonFileReader().read(temp_file_name)
        finally:
            # Удаление временного файла вручную после использования
            if os.path.exists(temp_file_name):
                os.remove(temp_file_name)

    def test_number_biggest(self):
        data = {
                "Иванов Иван Иванович": {
                    'математика': 101,
                    'литература': 100,
                    'программирование': 91
                }
        }

        # Создание временного файла и запись данных
        with tempfile.NamedTemporaryFile('w+',
                                         suffix='.json',
                                         delete=False,
                                         encoding='utf-8') as temp_file:
            json.dump(data, temp_file, ensure_ascii=False, indent=4)
            temp_file_name = temp_file.name  # Сохраняем имя файла
        try:
            with self.assertRaises(ValueError):
                JsonFileReader().read(temp_file_name)
        finally:
            # Удаление временного файла вручную после использования
            if os.path.exists(temp_file_name):
                os.remove(temp_file_name)
