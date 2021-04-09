import pathlib
import pandas
import book
from json import dump


def MAIN_MENU_OPTIONS():
    return ["Search for a book", "Move a book", "Quit"]


def SEARCH_MENU_OPTIONS():
    return ["Author", "Title", "Publisher", "Shelf", "Category", "Subject"]


def dump_dictionary_to_file(converted_json):
    with open('somebooks.json', 'w+') as file_object:
        dump(converted_json, file_object)


def convert_excel_to_json(excel_file):
    with open(excel_file):
        excel_data = pandas.read_excel(excel_file)
        converted_json = excel_data.to_json()
        dump_dictionary_to_file(converted_json)


def choice_checker(option_list):
    choice_list = list(enumerate(option_list, start=1))
    for choice in choice_list:
        print(f'{choice[0]}. {choice[1]}')
    user_choice = int(input("Enter a number: "))
    number_list = [number + 1 for number in range(len(option_list))]
    while user_choice not in number_list:
        print(f'Input is not an option, please try again.')
        user_choice = int(input("Enter a number: "))
    return user_choice


def ask_for_query(user_choice, menu_option):
    user_query = input(f'Enter the {menu_option[user_choice - 1]} to search: ')
    return user_query


def search_book():
    print(f'What would like to search for?')
    user_choice = choice_checker(SEARCH_MENU_OPTIONS())
    user_query = ask_for_query(user_choice, SEARCH_MENU_OPTIONS())

search_book()


def main_menu_selection():
    print(f'What would you like to do?')
    user_choice = choice_checker(MAIN_MENU_OPTIONS())
    if user_choice == 1:
        search_book()
    elif user_choice == 2:
        return 2
    return "quit"

# main_menu_selection()


def book_manager():
    path = pathlib.Path("somebooks.json")
    if path.exists():
        with open(path):
            pass
    else:
        convert_excel_to_json("somebooks.xlsx")
    user_choice = main_menu_selection()
    while user_choice != "quit":
        break


def main():
    """Execute the program"""
    book_manager()

#
# if __name__ == '__main__':
#     main()
