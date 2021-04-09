import pathlib
import pandas
from json import dump


def dump_dictionary_to_file(converted_json):
    with open('somebooks.json', 'w+') as file_object:
        dump(converted_json, file_object)


def convert_excel_to_json(excel_file):
    with open(excel_file):
        excel_data = pandas.read_excel(excel_file)
        converted_json = excel_data.to_json()
        dump_dictionary_to_file(converted_json)
        # return converted_json


def check_json_file():
    path = pathlib.Path("somebooks.json")
    if path.exists():
        with open(path):
            pass
    else:
        convert_excel_to_json("somebooks.xlsx")


def book_manager():
    check_json_file()


def main():
    """Execute the program"""
    book_manager()


if __name__ == '__main__':
    main()
