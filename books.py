import pathlib
import pandas
from book import Book
from json import dump, load


def MAIN_MENU_OPTIONS():
    return ["Search for a book", "Move a book", "Quit"]


def SEARCH_MENU_OPTIONS():
    return ["Author", "Title", "Publisher", "Shelf", "Category", "Subject"]


def create_book_object():
    with open('somebooks.json') as file_object:
        somebooks_dict = load(file_object)

    book_collection = []
    for book_num, book_dict in somebooks_dict.items():
        book = Book(
            author=book_dict["Author"],
            title=book_dict["Title"],
            publisher=book_dict["Publisher"],
            shelf=book_dict["Shelf"],
            category=book_dict["Category"],
            subject=book_dict["Subject"])
        book_collection.append(book)
    return book_collection


def write_dictionary_to_file(converted_json):
    with open('somebooks.json', 'w+') as file_object:
        file_object.write(converted_json)
    book_collection = create_book_object()
    return book_collection


def convert_excel_to_json(excel_file):
    with open(excel_file):
        excel_data = pandas.read_excel(excel_file)
        converted_json = excel_data.T.to_json()  # using transpose
        print("converted json type: ", type(converted_json))
        book_collection = write_dictionary_to_file(converted_json)
        return book_collection


def choice_validate(option_list):
    choice_list = list(enumerate(option_list, start=1))
    for choice in choice_list:
        print(f'{choice[0]}. {choice[1]}')
    user_choice = int(input("Enter a number: "))
    number_list = [number + 1 for number in range(len(option_list))]
    while user_choice not in number_list:
        print(f'Input is not an option, please try again.')
        user_choice = int(input("Enter a number: "))
    return user_choice


def ask_for_query(user_chosen_category):
    user_query = input(f'Type the {user_chosen_category} you want to search: ')
    return user_query


dict_json = {"Author": {"0": "Apri", "1": "Sean", "2": "nina"}, "Title": {"0": "book0", "1": "book1", "2": "book2"}}


def find_query(book_collection, user_query, user_menu_choice_category):
    category = user_menu_choice_category.lower()
    filtered_list = []
    for book in book_collection:
        attr = getattr(book, category)
        if user_query in attr.lower():
            filtered_list.append(book)
    return filtered_list


def search_book(book_collection):
    print(f'What would like to search for?')
    user_menu_choice_num = choice_validate(SEARCH_MENU_OPTIONS())
    user_menu_choice_category = SEARCH_MENU_OPTIONS()[user_menu_choice_num - 1]
    user_query = (ask_for_query(user_menu_choice_category)).lower()
    filtered_list = find_query(book_collection, user_query, user_menu_choice_category)


# search_book()


def main_menu_selection(book_collection):
    print(f'What would you like to do?')
    user_choice = choice_validate(MAIN_MENU_OPTIONS())
    if user_choice == 1:
        search_book(book_collection)
    elif user_choice == 2:
        return 2
    return "quit"


# main_menu_selection()


def book_manager():
    path = pathlib.Path("somebooks.json")
    if path.exists():
        book_collection = create_book_object()
    else:
        book_collection = convert_excel_to_json("somebooks.xlsx")
    user_choice = main_menu_selection(book_collection)
    while user_choice != "quit":
        break


def main():
    """Execute the program"""
    book_manager()


if __name__ == '__main__':
    main()
