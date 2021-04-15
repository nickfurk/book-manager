from unittest import TestCase
from book import Book


class TestBook(TestCase):

    def setUp(self):
        self.book_one = Book("123", "April C", "Hacking with April", "Chris", 9, "science", "computer")
        self.book_two = Book("456", "Lipra", "Coding with April", "Johnson", 10, "math", "matrix")

    def test__str__book_one_correct_string(self):
        actual = self.book_one.__str__()
        expected = f'\u001b[32;1mAuthor\u001b[0m: April C, \u001b[32;1mTitle\u001b[0m: Hacking with April, \u001b[' \
                   f'32;1mPublisher\u001b[0m: Chris, \u001b[32;1mShelf\u001b[0m: 9, ' \
                   f'\u001b[32;1mCategory\u001b[0m: science, \u001b[32;1mSubject\u001b[0m: computer, ' \
                   f'\u001b[32;1mid\u001b[0m: 123 '
        self.assertEqual(actual, expected)

    def test_to_dict_return_dictionary(self):
        actual = self.book_two.to_dict()
        expected = {
            "Author": "Lipra",
            "Title": "Coding with April",
            "Publisher": "Johnson",
            "Shelf": 10,
            "Category": "math",
            "Subject": "matrix"
        }
        self.assertEqual(actual, expected)
