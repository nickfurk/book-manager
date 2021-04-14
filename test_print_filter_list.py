import io
from unittest import TestCase
from unittest.mock import patch
from books import print_filter_list
from book import Book


class TestPrintFilterList(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_filter_list(self, mock_output):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", 9, "science", "computer")
        filtered_list = [book_1]
        print_filter_list(filtered_list)
        string = f'\nNumber of results: {len(filtered_list)}\n'
        expected = f'\u001b[33;1m{string}\u001b[0m\n1. ' \
                   f'\u001b[32;1mAuthor\u001b[0m: April C, \u001b[32;1mTitle\u001b[0m: Hacking with April, ' \
                   f'\u001b[32;1mPublisher\u001b[0m: Chris, \u001b[32;1mShelf\u001b[0m: 9, ' \
                   f'\u001b[32;1mCategory\u001b[0m: science, \u001b[32;1mSubject\u001b[0m: computer, ' \
                   f'\u001b[32;1mid\u001b[0m: 123 \n'
        self.assertEqual(mock_output.getvalue(), expected)

    def test_print_filter_list_return_list(self):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")
        filtered_list = [book_1]
        actual = print_filter_list(filtered_list)
        self.assertEqual(type(actual), list)
