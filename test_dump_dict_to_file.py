from unittest import TestCase
from unittest.mock import patch, mock_open
from books import dump_dict_to_file, JSON_FILENAME


class TestDumpDictToFile(TestCase):

    def test_dump_dict_to_file_open(self):
        with patch('builtins.open', mock_open()) as mocked_open:
            dump_dict_to_file({})
            mocked_open.assert_called_once_with(JSON_FILENAME(), 'w')

    @patch('books.dump')
    def test_dump_dict_to_file_dump_function_called(self, mock_dump):
        with patch('builtins.open', mock_open()) as mocked_open:
            dump_dict_to_file({})
            mock_file = mocked_open()
            mock_dump.assert_called_once_with({}, mock_file,  indent=4)



