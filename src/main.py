# -*- coding: utf-8 -*-
import argparse

import sys

from CalcRating import CalcRating

from CalcInfo import CalcInfo

from YamlFileReader import YamlFileReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, default="../data/data.yml",
                        required=False, help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    yaml_reader = YamlFileReader()
    students = yaml_reader.read(path)
    print("Students: ", students)
    print(type(students))
    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    calc_high_rating = CalcInfo(students).calc_high_rating()
    print(calc_high_rating)


if __name__ == "__main__":
    main()
