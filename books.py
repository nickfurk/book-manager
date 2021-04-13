import pathlib
import pandas
from book import Book
from json import dump, load


def JSON_FILENAME():
    return "somebooks.json"


def EXCEL_FILENAME():
    return "somebooks.xlsx"


def MAIN_MENU_OPTIONS():
    return ["Search for a book", "Move a book", "Quit"]


def SEARCH_MENU_OPTIONS():
    return ["Author", "Title", "Publisher", "Shelf", "Category", "Subject"]


def change_none_to_string(somebooks_dict):
    for book_num, book_dict in somebooks_dict.items():
        if book_dict["Publisher"] is None:
            book_dict["Publisher"] = "None"
    return somebooks_dict


def create_book_object():
    with open(JSON_FILENAME()) as file_object:
        somebooks_dict = load(file_object)

    updated_somebooks_dict = change_none_to_string(somebooks_dict)

    book_collection = []
    for book_num, book_dict in updated_somebooks_dict.items():
        book = Book(
            id=book_num,
            author=book_dict["Author"],
            title=book_dict["Title"],
            publisher=book_dict["Publisher"],
            shelf=book_dict["Shelf"],
            category=book_dict["Category"],
            subject=book_dict["Subject"])
        book_collection.append(book)
    return book_collection

    # book_collection = []
    # for book_num, book_dict in somebooks_dict.items():
    #     book = Book(
    #         id=book_num,
    #         author=book_dict["Author"],
    #         title=book_dict["Title"],
    #         publisher=book_dict["Publisher"],
    #         shelf=book_dict["Shelf"],
    #         category=book_dict["Category"],
    #         subject=book_dict["Subject"])
    #     book_collection.append(book)
    # return book_collection


def write_dictionary_to_file(converted_json):
    with open(JSON_FILENAME(), 'w+') as file_object:
        file_object.write(converted_json)
    book_collection = create_book_object()
    return book_collection


def convert_excel_to_json(excel_file):
    with open(excel_file):
        excel_data = pandas.read_excel(excel_file)
        converted_json = excel_data.T.to_json(indent=4)  # using transpose
        book_collection = write_dictionary_to_file(converted_json)
        return book_collection


def choice_validate(option_list):
    choice_list = list(enumerate(option_list, start=1))
    for choice in choice_list:
        print(f'{choice[0]}. {choice[1]}')
    user_choice = input("\nEnter a number: \n")
    number_list = str([number + 1 for number in range(len(option_list))])
    while user_choice not in number_list or user_choice == "":
        print(f'Input is not an option, please try again.')
        user_choice = input("Enter a number: ")
    return user_choice


def ask_for_query(user_chosen_category):
    user_query = input(f'Enter the {user_chosen_category} you want to search: ')
    while user_query == "":
        user_query = input(f'Invalid entry, enter the {user_chosen_category} you want to search: ')
    return user_query


def find_query(book_collection, user_query, user_menu_choice_category):
    category = user_menu_choice_category.lower()
    if category == "shelf" and user_query.isnumeric():
        user_query = int(user_query)
    elif category == "shelf" and user_query.isnumeric() is False:
        user_query = user_query.title()

    filtered_list = []
    for book in book_collection:
        attr = getattr(book, category)  # to get category before the .lower
        if attr is not None and category != "shelf" and user_query in attr.lower():
            filtered_list.append(book)
        elif category == "shelf" and user_query == book.shelf:
            filtered_list.append(book)
    return filtered_list


def print_filter_list(filtered_list):
    string = f'\nNumber of results: {len(filtered_list)}\n'
    print(f'\u001b[33;1m{string}\u001b[0m')
    full_info_list = [str(book) for book in filtered_list]
    print_list = list(enumerate(full_info_list, start=1))
    for element in print_list:
        print(f'{element[0]}. {element[1]}')
    return print_list


def search_book(book_collection):
    user_menu_choice_num = choice_validate(SEARCH_MENU_OPTIONS())
    user_menu_choice_category = SEARCH_MENU_OPTIONS()[int(user_menu_choice_num) - 1]
    user_query = (ask_for_query(user_menu_choice_category)).lower()
    filtered_list = find_query(book_collection, user_query, user_menu_choice_category)
    print_filter_list(filtered_list)
    return filtered_list


def shelf_choices(book_collection):
    shelf_num = []
    for book in book_collection:
        shelf_num.append(book.shelf)
    print((list(set(shelf_num))))
    return shelf_num


def move_book_no_result_retry(filtered_list, book_collection):
    while not filtered_list:
        print('There are no results, please retry so we can move the book after.\n')
        filtered_list = search_book(book_collection)
    return filtered_list


def input_error_retry(user_input, filtered_list):
    while not user_input.isdigit() or int(user_input) > len(filtered_list) or user_input == "0":
        user_input = (input(f'That is an invalid input, enter number again: \n'))
    return user_input


def shelf_input_retry_and_convert(user_shelf_input: str, shelf_options: list):
    """Check correct user input.

    Function verifies if user input is among the shelf options available. If not, then function asks the user for an
    input again. If the user input is among th shelf options, then it will convert the string input into a titled
    string, or it will convert the string into an integer if the string is numeric. User input gets returned.

    :param user_shelf_input: a string
    :param shelf_options: a list
    :precondition: user_shelf_input: must be a string that represents a shelf name or number
    :precondition: shelf_options is a list of available shelf options
    :postcondition: correctly asks the user to re-enter if prior their user_shelf_input is not in shelf_options
    :postcondition: correctly coverts available user_shelf_input to a title string if the input is a word
    :postcondition: correctly coverts available user_shelf_input to an integer if the string is numeric
    :return: user input that is either an integer or a string
    """
    while user_shelf_input not in shelf_options:
        print(f'Invalid shelf, please enter the correct shelf information.')
        user_shelf_input = (input(f'\nType your shelf preference:')).title()
    if user_shelf_input.isnumeric():
        user_shelf_input = int(user_shelf_input)
    return user_shelf_input


def move_book(book_collection: list):
    """Move book feature flow.

    Function acts as a flow for the move book feature. A series of functions are called to accomplish this.
    At the very end, the object book shelf gets updated with the new shelf information. Functions that are
    called are related to finding a filtered list of books, choosing which book to move, choose which shelf
    to move the book to, update book object with the new shelf information, and then returning to the main menu.

    :param book_collection: a list
    :precondition: book_collection has to be a list of object book
    :postcondition: correctly call functions related to the move book feature and updates the object book shelf
    :return: None
    """
    filtered_list = search_book(book_collection)
    verify_filtered_list = move_book_no_result_retry(filtered_list, book_collection)
    user_input = (input(f'\nChoose which book to move, enter number: \n'))
    verify_user_input = input_error_retry(user_input, verify_filtered_list)
    selected_book = verify_filtered_list[int(verify_user_input) - 1]
    print(f'You have selected >>> {selected_book}\n\nWhich shelf do you want to move the book to? See options below:\n')
    shelf_options = str(shelf_choices(book_collection))
    user_shelf_input = (input(f'\nType in your preference: ')).title()
    verify_user_shelf_input = shelf_input_retry_and_convert(user_shelf_input, shelf_options)
    selected_book.shelf = verify_user_shelf_input
    print(f'\n\u001b[33;1mBook shelf updated!\u001b[0m >>> {selected_book}')
    main_menu_selection(book_collection)


def dump_dict_to_file(output_dict: dict):
    """Dump dictionary to a json file.

    :param output_dict: a dictionary
    :precondition: output_dict is a dictionary of the books
    :postcondition: correctly dump the output_dict dictionary into the json file in json format
    :return:None
    """
    with open(JSON_FILENAME(), "w") as out_file:
        dump(output_dict, out_file, indent=4)
    print(f'\n\u001b[33;1mData saved. See you later!\u001b[0m\n')


def list_to_dict(book_collection: list):
    """Convert a list with objects into a dictionary.

    Function converts a list with objects into a dictionary, then calls dump_dict_to_file function.

    :param book_collection: a list with book objects
    :precondition: book_collection has to be a list with book objects
    :postcondition: correctly converts a list with book objects into a dictionary
    :return: None
    """
    output_dict = {}
    for book in book_collection:
        output_dict[book.id] = book.to_dict()
    dump_dict_to_file(output_dict)

    # with open(JSON_FILENAME(), "w") as out_file:
    #     dump(output_dict, out_file, indent=4)
    # print(f'\n\u001b[33;1mData saved. See you later!\u001b[0m\n')


def main_menu_selection(book_collection: list):
    """Main menu selection.

    Function asks the user what they would like to do and calls choice_validate function to get user input.
    After the user inputs a number between 1 to 3 inclusive, it takes the user down different paths.

    :param book_collection: a list with book objects
    :precondition: book_collection must be a list with book objects
    :postcondition: correctly calls different functions depending what the user selects. If select choice "1",
                    function will call search_book and then main_menu_selection. If select choice "2", function
                    will call move_book. If select choice "3" function will call save.
    :return: None
    """
    print(f'\nWhat would you like to do?\n')
    user_choice = choice_validate(MAIN_MENU_OPTIONS())
    if user_choice == "1":
        print(f'\nWhat would like to search for?\n')
        search_book(book_collection)
        main_menu_selection(book_collection)
    if user_choice == "2":
        print(f'\nLet\'s find your desired book first, before we move it. Select an attribute.\n')
        move_book(book_collection)
    if user_choice == "3":
        list_to_dict(book_collection)


# def check_for_file():
#     path = pathlib.Path("somebooks.json")
#     if path.exists():
#         book_collection = create_book_object()
#         main_menu_selection(book_collection)
#     else:
#         book_collection = convert_excel_to_json("somebooks.xlsx")
#         main_menu_selection(book_collection)

def get_book_collection() -> list:
    """Get a list of book objects.

    Function checks if a json file is available. If it is the it will call create_book_object() function,
    if not, it will call a convert_excel_to_json function. A list of book object returns.

    :return: a list of book objects
    """
    path = pathlib.Path(JSON_FILENAME())
    if path.exists():
        book_collection = create_book_object()
    else:
        book_collection = convert_excel_to_json(EXCEL_FILENAME())
    return book_collection


def main():
    """Execute the program"""
    # check_for_file()
    book_collection = get_book_collection()
    main_menu_selection(book_collection)


if __name__ == '__main__':
    main()
