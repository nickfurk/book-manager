import io
from unittest import TestCase
from unittest.mock import patch
from books import shelf_choices
from book import Book


class TestShelfChoices(TestCase):

    # COME BACK AND FIX!!!!!!!!!!!!
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_shelf_choices_print_shelf_list(self, mock_output):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", 1, "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", 2, "math", "matrix")
        book_collection = [book_1, book_2]
        shelf_choices(book_collection)
        expected = f'{[book_1.shelf, book_2.shelf]}\n'
        self.assertEqual(mock_output.getvalue(), expected)

    def test_shelf_choices_return_self_list(self):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", 1, "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", 2, "math", "matrix")
        book_collection = [book_1, book_2]
        actual = shelf_choices(book_collection)
        expected = [book_1.shelf, book_2.shelf]
        self.assertEqual(actual, expected)
