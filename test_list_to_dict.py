from book import Book
from unittest import TestCase
from unittest.mock import patch
from books import list_to_dict


class TestSave(TestCase):

    @patch('books.dump_dict_to_file')
    def test_list_to_dict_convert_to_dict(self, dump_dict_to_file):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")
        book_collection_list = [book_1]
        list_to_dict(book_collection_list)
        dump_dict_to_file.assert_called_with({'123': {'Author': 'April C', 'Title': 'Hacking with April', 'Publisher':
            'Chris', 'Shelf': '9', 'Category': 'science', 'Subject': 'computer'}})
