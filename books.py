import pathlib
import pandas
import book
from json import dump


def MAIN_MENU_OPTIONS():
    return ["Search for a book", "Move a book", "Quit"]


def dump_dictionary_to_file(converted_json):
    with open('somebooks.json', 'w+') as file_object:
        dump(converted_json, file_object)


def convert_excel_to_json(excel_file):
    with open(excel_file):
        excel_data = pandas.read_excel(excel_file)
        converted_json = excel_data.to_json()
        dump_dictionary_to_file(converted_json)


def choice_checker(option_list):
    print(list(enumerate(option_list, start=1)))
    user_choice = int(input("What would you like to do? Enter a number: "))
    number_list = [number + 1 for number in range(len(option_list))]
    while user_choice not in number_list:
        print(f'Input is not an option, please try again.')
        user_choice = int(input("Enter a number: "))
    return user_choice


def main_menu_selection():
    user_choice = choice_checker(MAIN_MENU_OPTIONS())
    if user_choice == 1:
        return 1
    elif user_choice == 2:
        return 2
    else:
        return "quit"


def book_manager():
    path = pathlib.Path("somebooks.json")
    if path.exists():
        with open(path):
            pass
    else:
        convert_excel_to_json("somebooks.xlsx")
    while True:
        main_menu()



# def book_manager():
#     check_json_file()


def main():
    """Execute the program"""
    book_manager()

#
# if __name__ == '__main__':
#     main()
