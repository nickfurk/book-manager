from unittest.mock import patch, Mock
from unittest import TestCase
from books import get_book_collection


class TestGetBookCollection(TestCase):

    @patch('books.create_book_object')
    @patch('books.pathlib.Path', return_value=Mock())
    def test_create_book_object_is_called(self, mock_pathlib_path, mock_create_book_object):
        path = mock_pathlib_path.return_value
        path.exists.return_value = True
        get_book_collection()
        mock_create_book_object.assert_called_with()

    @patch('books.convert_excel_to_json')
    @patch('books.pathlib.Path', return_value=Mock())
    def test_convert_excel_to_json_is_called(self, mock_pathlib_path, mock_convert_excel_to_json):
        path = mock_pathlib_path.return_value
        path.exists.return_value = False
        get_book_collection()
        mock_convert_excel_to_json.assert_called_with('somebooks.xlsx')

    def test_return_a_list(self):
        actual = get_book_collection()
        self.assertEqual(type(actual), list)
