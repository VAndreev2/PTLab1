import argparse
import json
import os
import sys
import unittest
import tempfile
sys.path.insert(1, os.path.join(sys.path[0], '../src'))
from JsonFileReader import JsonFileReader  # noqa: E402


class test_JsonFileReader(unittest.TestCase):

    @staticmethod
    def get_path_from_arguments(args) -> str:
        parser = argparse.ArgumentParser()
        parser.add_argument('filename', nargs='?',
                            default='/home/user/PTLab1/data/data.json')
        parser.add_argument('unittest_args', nargs='*')
        args = parser.parse_args(args)
        sys.argv[1:] = args.unittest_args
        return args.filename

    def create_temp_file(self, data):
        with tempfile.NamedTemporaryFile('w+', suffix='.json',
                                         delete=False,
                                         encoding='utf-8') as temp_file:
            json.dump(data, temp_file, ensure_ascii=False, indent=4)
            temp_file_name = temp_file.name  # Сохраняем имя файла
            return temp_file_name

    def reader_for_test(self, temp_file_name):
        try:
            with self.assertRaises(ValueError):
                JsonFileReader().read(temp_file_name)
        finally:
            # Удаление временного файла вручную после использования
            if os.path.exists(temp_file_name):
                os.remove(temp_file_name)

    def test_read(self):
        path = self.get_path_from_arguments(sys.argv[1:])
        # Ожидаемый результат
        expected_result = {
            'Иванов Иван Иванович': [('математика', 67),
                                     ('литература', 100),
                                     ('программирование', 91)],
            'Петров Петр Петрович': [('математика', 78),
                                     ('химия', 87),
                                     ('социология', 61)]
        }
        self.assertEqual(
            JsonFileReader().read(
                path
            ),
            expected_result
        )

    def test_desc_type(self):

        data = {
            'Иванов Иван Иванович': {
                'математика': '123',
                'литература': 100,
                'программирование': 91
            }
        }
        # Создание временного файла и запись данных
        temp_file = self.create_temp_file(data)
        self.reader_for_test(temp_file)

    def test_number_negative(self):

        data = {
            "Иванов Иван Иванович": {
                'математика': 67,
                'литература': -100,
                'программирование': 91
            }
        }

        # Создание временного файла и запись данных
        temp_file = self.create_temp_file(data)
        self.reader_for_test(temp_file)

    def test_number_biggest(self):
        data = {
            "Иванов Иван Иванович": {
                'математика': 101,
                'литература': 100,
                'программирование': 91
            }
        }

        # Создание временного файла и запись данных
        temp_file = self.create_temp_file(data)
        self.reader_for_test(temp_file)


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]], exit=False)
