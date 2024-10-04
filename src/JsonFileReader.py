# -*- coding: utf-8 -*-
import json

from Types import DataType
from DataReader import DataReader


class JsonFileReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        students: DataType = {}

        with open(path, 'r', encoding='utf-8') as file:
            # Load data from JSON file
            data = json.load(file)

        if not data:
            raise ValueError("Файл пустой или не содержит данных.")

        # Validate and parse data
        for student, subjects in data.items():

            for subj, score in subjects.items():
                if not isinstance(subj, str) or not isinstance(score, int):
                    raise ValueError("Предметы должны быть строками, "
                                     "а оценки - целыми числами.")
                if score > 100 or score < 0:
                    raise ValueError

            students[student] = [(subj, score)
                                 for subj, score in
                                 subjects.items()]

        return students
