import pathlib
import pandas
import json
import doctest
from book import Book
from json import dump


def JSON_FILENAME() -> str:
    """Name of the json file.

    :return: a string
    """
    return "somebooks.json"


def EXCEL_FILENAME() -> str:
    """Name of the excel file.

    :return: a string
    """
    return "somebooks.xlsx"


def MAIN_MENU_OPTIONS() -> list:
    """Main menu options.

    :return: a list
    """
    return ["Search for a book", "Move a book", "Quit"]


def SEARCH_MENU_OPTIONS() -> list:
    """Search menu options.

    :return: a list
    """
    return ["Author", "Title", "Publisher", "Shelf", "Category", "Subject"]


def change_none_to_string(somebooks_dict: dict) -> dict:
    """Change None value in Publisher key to string.

    :param somebooks_dict: a dictionary
    :precondition: somebooks_dict is a dictionary that contain book information and likely to a key "Publisher"
    :postcondition: correctly converts key Publisher value None to a string
    :return: a dictionary that is updated with the None string

    >>> some_dict = {"1": {"Publisher": None}}
    >>> change_none_to_string(some_dict)
    {'1': {'Publisher': 'None'}}
    """
    for book_num, book_dict in somebooks_dict.items():
        if book_dict["Publisher"] is None:
            book_dict["Publisher"] = "None"
    return somebooks_dict


def read_from_json_file() -> list:
    """Read from a json file.

    Function opens and reads from a json file. It loads the file content into a string.
    The string is passed into the function create_book_object in order to return a list
    of Book objects.

    :return: a list of Book objects
    """
    with open(JSON_FILENAME(), "r") as file_object:
        json_string = file_object.read()
    book_collection = create_book_object(json_string)
    return book_collection


def create_book_object(json_string: str) -> list:
    """Create Book objects in a list.

    Function takes a json string and convert it into a dictionary. The dictionary gets iterated
    to create Book objects. Book objects are appended to a list. Return list.

    :param json_string: a string
    :precondition: json_string is the string that represents the excel data
    :postcondition: correctly create Book objects and append it to a list
    :return: a list with Book objects
    """
    somebooks_dict = json.loads(json_string)
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


def convert_excel_to_json(excel_file: str) -> list:
    """Convert excel file to json.

    Function converts excel file to json and then calls write_dictionary_to_file to get
    a list of Book objects. Returns list of Book objects.

    :param excel_file: a string
    :precondition: excel_file must a string that represents an excel file name
    :postcondition: correctly coverts excel file data to json format
    :return: a list of Book objects
    """
    excel_data = pandas.read_excel(excel_file)
    converted_json = excel_data.T.to_json(indent=4)  # using transpose
    book_collection = create_book_object(converted_json)
    return book_collection


def choice_validate(option_list: list) -> str:
    """Check user choice.

    Function checks if user choice is from a list of available options, if available then return user choice,
    else asks user to re-enter

    :param option_list: a list
    :precondition: option_list should be a list with available options for the user to choose from
    :postcondition: correctly check if user input is from a list of available options, if not asks user to
                    re-enter, else return string
    :return: a string
    """
    choice_list = list(enumerate(option_list, start=1))
    for choice in choice_list:
        print(f'{choice[0]}. {choice[1]}')
    user_choice = input("\nEnter a number: \n")
    number_list = str([number + 1 for number in range(len(option_list))])
    while user_choice not in number_list or user_choice == "":
        print(f'Input is not an option, please try again.')
        user_choice = input("Enter a number: ")
    return user_choice


def ask_for_query(user_chosen_category: str) -> str:
    """Get user input and verify input.

    Function asks for user input. If user hits enter without typing anything, then will ask the user to re-enter.

    :param user_chosen_category: a string
    :precondition: user_chosen_category could be string author, title, publisher, shelf, category or subject
    :postcondition: verifies if user input is a non-empty string, if empty then ask user to re-enter, else return string
    :return: a string
    """
    user_query = input(f'Enter the {user_chosen_category} you want to search: ')
    while user_query == "":
        user_query = input(f'Invalid entry, enter the {user_chosen_category} you want to search: ')
    return user_query


def check_if_shelf_category(category: str, user_query: str):
    """Convert string to int or title string.

    :param category: a string
    :param user_query: a string
    :precondition: category string should be "shelf"
    :postcondition: correctly coverts the string to integer if the string is numeric, else change string to titled
    :return: a string or an integer

    >>> picked_category = "shelf"
    >>> user_entry = "2"
    >>> check_if_shelf_category(picked_category, user_entry)
    2

    >>> picked_category = "shelf"
    >>> user_entry = "gaby"
    >>> check_if_shelf_category(picked_category, user_entry)
    'Gaby'
    """
    if category == "shelf" and user_query.isnumeric():
        user_query = int(user_query)
    elif category == "shelf" and user_query.isnumeric() is False:
        user_query = user_query.title()
    return user_query


def find_query(book_collection: list, user_query: str, user_menu_choice_category: str) -> list:
    """Match user query in book collection and return a filtered list of object Book(s).

    Function matches user query to the specify category in the book collection and returns a list of
    books that contains the query.

    :param book_collection: a list
    :param user_query: a string
    :param user_menu_choice_category: a string
    :precondition: book_collection has to be a list of Book objects
    :precondition: user_query is a string that the user is interested in searching
    :precondition: user_menu_choice_category: a string that the user wants to search
    :postcondition: correctly returns the filtered list of Books object(s) in a list
    :return: a list of filtered Book object(s)
    """
    category = user_menu_choice_category.lower()
    user_query = check_if_shelf_category(category, user_query)

    filtered_list = []
    for book in book_collection:
        attr = getattr(book, category)  # to get category before the .lower
        if attr is not None and category != "shelf" and user_query in attr.lower():
            filtered_list.append(book)
        elif category == "shelf" and user_query == book.shelf:
            filtered_list.append(book)
    return filtered_list


def print_filter_list(filtered_list: list):
    """Print filter list.

    Function takes in a filtered Book object list, prints out the object as numbered list, and return the print list.

    :param filtered_list: a list
    :precondition: filtered_list is a list of filtered Book object(s)
    :postcondition: correctly prints out the book objects in filtered_list as numbered list and return the print list
    :return: a list
    """
    string = f'\nNumber of results: {len(filtered_list)}\n'
    print(f'\u001b[33;1m{string}\u001b[0m')
    full_info_list = [str(book) for book in filtered_list]
    print_list = list(enumerate(full_info_list, start=1))
    for element in print_list:
        print(f'{element[0]}. {element[1]}')


def search_book(book_collection: list) -> list:
    """Search book(s) and return filtered book list.

    Function acts as a flow for the search book feature. The functions calls choice_validate to ensure that
    user's input is an available category choice, then calls ask_for_query for the user to input their query,
    find_query is called next to return the filtered list of Book object(s).

    :param book_collection: a list
    :precondition: book_collection has to be a list with Book objects
    :postcondition: correctly returns a filtered list of Book objects based on user's chosen category choice and query
    :return: a list of filtered Book object(s)
    """
    user_menu_choice_num = choice_validate(SEARCH_MENU_OPTIONS())
    user_menu_choice_category = SEARCH_MENU_OPTIONS()[int(user_menu_choice_num) - 1]
    user_query = (ask_for_query(user_menu_choice_category)).lower()
    filtered_list = find_query(book_collection, user_query, user_menu_choice_category)
    print_filter_list(filtered_list)
    return filtered_list


def shelf_choices(book_collection: list) -> list:
    """Return list of book.shelf.

    Function takes a book_collection list that has all the Book objects and then creates another list with only
    book.shelf.

    :param book_collection: a list
    :preconditon: book_collection is a list of Book objects
    :postcondition: correctly return a list of Book.shelf from all the Book in book_collection
    :return: a list of book.shelf

    >>> book_1 = Book("123", "April C", "Hacking with April", "Chris", 1, "science", "computer")
    >>> book_2 = Book("456", "Lipra", "Coding with April", "Johnson", 2, "math", "matrix")
    >>> book_list = [book_1, book_2]
    >>> shelf_choices(book_list)
    [1, 2]
    [1, 2]
    """
    shelf_num = []
    for book in book_collection:
        shelf_num.append(book.shelf)
    print((list(set(shelf_num))))
    return shelf_num


def move_book_no_result_retry(filtered_list: list, book_collection: list) -> list:
    """Check if filtered list has Book object(s).

    Function checks if filtered list has book object(s), if not will ask the user to re-enter input, else returns
    filtered list.

    :param filtered_list: a list
    :param book_collection: a list
    :precondition: filtered_list is a list with Book object(s)
    :precondition: book_collect is a list with all Book objects
    :postcondition: correctly asks the user to re-enter if precondition for filtered_list is not met
    :return: a list with book object(s)
    """
    while not filtered_list:
        print('There are no results, please retry so we can move the book after.\n')
        filtered_list = search_book(book_collection)
    return filtered_list


def input_error_retry(user_input: str, filtered_list: list) -> str:
    """Check user input string.

    Function checks the user input string. If the string does not meet the user_input preconditions, then will ask
    the user to re-enter input.

    :param user_input: a string
    :param filtered_list: a list
    :precondition: user_input string should be numeric, not longer than the length of the filtered_list, and not "0"
    :precondition: filtered_list is a list that includes book objects
    :postcondition: correctly asks user to enter number again if the user_input string does not meet the precondition
    :return: string
    """
    while not user_input.isdigit() or int(user_input) > len(filtered_list) or user_input == "0":
        user_input = (input(f'That is an invalid input, enter number again: \n'))
    return user_input


def shelf_input_retry_and_convert(user_shelf_input: str, shelf_options: str):
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


def get_book_collection() -> list:
    """Get a list of book objects.

    Function checks if a json file is available. If it is the it will call create_book_object() function,
    if not, it will call a convert_excel_to_json function. A list of book object returns.

    :return: a list of book objects
    """
    path = pathlib.Path(JSON_FILENAME())
    if path.exists():
        book_collection = read_from_json_file()
    else:
        book_collection = convert_excel_to_json(EXCEL_FILENAME())
    return book_collection


def main():
    """Execute the program"""
    doctest.testmod(verbose=True)
    book_collection = get_book_collection()
    main_menu_selection(book_collection)


if __name__ == '__main__':
    main()
