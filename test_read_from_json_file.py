from unittest import TestCase
from unittest.mock import patch, mock_open
from books import read_from_json_file, JSON_FILENAME


class TestReadFromJsonFile(TestCase):

    @patch('books.create_book_object')
    def test_read_from_json_file_open_file(self, mock_create_book_object):
        with patch('builtins.open', mock_open()) as mocked_open:
            read_from_json_file()
            mocked_open.assert_called_once_with(JSON_FILENAME(), 'r')

    @patch('books.create_book_object')
    def test_read_from_json_file_create_book_object_called(self, mock_create_book_object):
        with patch('builtins.open', mock_open()) as mocked_open:
            read_from_json_file()
            mock_create_book_object.assert_called_once_with('')
