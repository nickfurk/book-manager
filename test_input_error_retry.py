import io
from book import Book
from unittest import TestCase
from unittest.mock import patch
from books import input_error_retry


class TestInputErrorRetry(TestCase):

    @patch('builtins.input')
    def test_input_error_retry_wrong_input_not_digit(self, mock_input):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", "10", "math", "matrix")
        user_input = "asdf"
        filtered_list = [book_1, book_2]
        input_error_retry(user_input, filtered_list)
        mock_input.assert_called_with(f'That is an invalid input, enter number again: \n')

    @patch('builtins.input')
    def test_input_error_retry_wrong_input_string_zero(self, mock_input):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", "10", "math", "matrix")
        user_input = "0"
        filtered_list = [book_1, book_2]
        input_error_retry(user_input, filtered_list)
        mock_input.assert_called_with(f'That is an invalid input, enter number again: \n')

    @patch('builtins.input')
    def test_input_error_retry_wrong_input_out_of_index(self, mock_input):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", "10", "math", "matrix")
        user_input = "11"
        filtered_list = [book_1, book_2]
        input_error_retry(user_input, filtered_list)
        mock_input.assert_called_with(f'That is an invalid input, enter number again: \n')
