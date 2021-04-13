import io
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

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dump_dict_to_file_print_goodbye_message(self, mock_output):
        dump_dict_to_file({})
        expected = f'\n\u001b[33;1mData saved. See you later!\u001b[0m\n\n'
        self.assertEqual(mock_output.getvalue(), expected)
