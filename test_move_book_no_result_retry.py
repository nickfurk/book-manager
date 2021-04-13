import io
from unittest import TestCase
from unittest.mock import patch
from books import move_book_no_result_retry
from book import Book


class TestMoveBookNoResultRetry(TestCase):

    @patch('books.search_book', return_value=[Book("123", "April C", "Hacking with April", "Chris", "9", "science",
                                                   "computer")])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_book_no_result_retry_wrong_input_string(self, mock_output, mock_search_book):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", "10", "math", "matrix")
        filtered_list = []
        book_collection = [book_1, book_2]
        move_book_no_result_retry(filtered_list, book_collection)
        expected = 'There are no results, please retry so we can move the book after.\n\n'
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('books.search_book')
    def test_move_book_no_result_retry_wrong_search_book_called(self, mock_search_book):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", "10", "math", "matrix")
        filtered_list = []
        book_collection = [book_1, book_2]
        move_book_no_result_retry(filtered_list, book_collection)
        mock_search_book.assert_called_with(book_collection)

    @patch('books.search_book')
    def test_move_book_no_result_retry_correct_input(self, mock_search_book):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", "10", "math", "matrix")
        filtered_list = [book_2]
        book_collection = [book_1, book_2]
        actual = move_book_no_result_retry(filtered_list, book_collection)
        self.assertEqual(actual, filtered_list)
