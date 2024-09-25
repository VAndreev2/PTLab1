# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader

import yaml


class YamlFileReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        students: DataType = {}

        with open(path, 'r', encoding='utf-8') as file:

            # Загружаем данные YAML из файла
            data = yaml.safe_load(file)

            if not data:
                raise ValueError("Файл пустой.")

        # data - это список словарей, каждый словарь имеет одного студента
        for student_data in data:
            for student, subjects in student_data.items():
                if not isinstance(student, str):
                    raise ValueError("Имя студента должно быть строкой.")
                if not isinstance(subjects, dict):
                    raise ValueError("Предметы должны быть словарем.")
                for subj, score in subjects.items():
                    if not isinstance(subj, str) or not isinstance(score, int):
                        raise ValueError("Предметы должны "
                                         "быть строками, "
                                         "а оценки - "
                                         "целыми числами.")
                students[student] = [(subj, score)
                                     for subj, score in subjects.items()]

        return students
