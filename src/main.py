# -*- coding: utf-8 -*-
import argparse

import sys

from CalcRating import CalcRating

from JsonFileReader import JsonFileReader

from QuartRating import QuartRating


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str,
                        default="../data/data.yml",
                        required=False, help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    json_reader = JsonFileReader()
    students = json_reader.read(path)
    print("Students: ", students)
    print(type(students))
    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    quart_rating = QuartRating(rating).quart_students()
    print(quart_rating)


if __name__ == "__main__":
    main()
