from unittest import TestCase
from unittest.mock import patch
from books import search_book
from book import Book


class TestSearchBook(TestCase):

    @patch('books.find_query')
    @patch('books.ask_for_query')
    @patch('books.choice_validate')
    def test_search_book_choice_validate_called(self, mock_choice_validate, mock_ask_for_query, mock_find_query):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", 9, "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", 10, "math", "matrix")
        book_collection = [book_1, book_2]
        search_book(book_collection)
        mock_choice_validate.assert_called_with(['Author', 'Title', 'Publisher', 'Shelf', 'Category', 'Subject'])

    @patch('books.find_query')
    @patch('books.ask_for_query')
    @patch('books.choice_validate')
    def test_search_book_ask_for_query_called(self, mock_choice_validate, mock_ask_for_query, mock_find_query):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", 9, "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", 10, "math", "matrix")
        book_collection = [book_1, book_2]
        search_book(book_collection)
        mock_ask_for_query.assert_called_with('Author')

    @patch('books.find_query')
    @patch('books.ask_for_query')
    @patch('books.choice_validate')
    def test_search_book_find_query_called(self, mock_choice_validate, mock_ask_for_query, mock_find_query):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", 9, "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", 10, "math", "matrix")
        book_collection = [book_1, book_2]
        search_book(book_collection)
        user_query = (mock_ask_for_query()).lower()
        mock_find_query.assert_called_with(book_collection, user_query, 'Author')

    @patch('books.find_query')
    @patch('books.ask_for_query')
    @patch('books.choice_validate')
    def test_search_book_print_filter_return_list(self, mock_choice_validate, mock_ask_for_query, mock_find_query):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", 9, "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", 10, "math", "matrix")
        book_collection = [book_1, book_2]
        actual = search_book(book_collection)
        filtered_list = mock_find_query()
        self.assertEqual(actual, filtered_list)
