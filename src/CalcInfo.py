# -*- coding: utf-8 -*-
from Types import DataType

RatingType = dict[str, float]


class CalcInfo:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}


    def calc_high_rating(self) -> RatingType:
        high_students = 0
        for key in self.data:
            high_rating = True
            for subject in self.data[key]:
                if not isinstance(subject[1], int):
                    raise ValueError
                if subject[1] < 0 or subject[1] > 100:
                    raise ValueError
                if subject[1] < 90:
                    high_rating = False
                if not high_rating:
                    break
            if high_rating:
                high_students += 1

        return high_students
