# -*- coding: utf-8 -*-
import np

RatingType = dict[str, float]


class CalcInfo:

    def __init__(self, ratings: RatingType) -> None:
        self.ratings = ratings

    def quart_students(self) -> RatingType:

        if len(self.ratings) < 4:
            raise ValueError("Недостаточно данных для расчета. Минимум 4")
        # Получаем список всех рейтингов
        ratings_values = list(self.ratings.values())

        # Находим 75-й перцентиль (начало последнего квартиля)
        percentile_75 = np.percentile(ratings_values, 75)

        # Определяем студентов, чей рейтинг попадает в последний квартиль
        last_quartile_students = {name: rating
                                  for name, rating in self.ratings.items()
                                  if rating >= percentile_75}

        # Возвращаем список студентов
        return last_quartile_students
