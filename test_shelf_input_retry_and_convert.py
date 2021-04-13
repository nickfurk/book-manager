import io
from unittest import TestCase
from unittest.mock import patch
from books import shelf_input_retry_and_convert


class TestShelfInputRetryAndConvert(TestCase):

    @patch('builtins.input', return_value="Gaby")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_shelf_input_retry_and_convert_wrong_input_print(self, mock_output, mock_input):
        user_shelf_input = "asdf"
        shelf_options = ["Gaby", "1", "2", "3"]
        shelf_input_retry_and_convert(user_shelf_input, shelf_options)
        expected = f'Invalid shelf, please enter the correct shelf information.\n'
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('builtins.input', return_value="tera")
    # @patch('sys.stdout', new_callable=io.StringIO)
    def test_shelf_input_retry_and_convert_string_input_title(self, mock_input):
        user_shelf_input = "asdf"
        shelf_options = ["Gaby", "Tera", "1", "2", "3"]
        actual = shelf_input_retry_and_convert(user_shelf_input, shelf_options)
        expected = "Tera"
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="1")
    # @patch('sys.stdout', new_callable=io.StringIO)
    def test_shelf_input_retry_and_convert_integer_input(self, mock_input):
        user_shelf_input = "asdf"
        shelf_options = ["Gaby", "Tera", "1", "2", "3"]
        actual = shelf_input_retry_and_convert(user_shelf_input, shelf_options)
        self.assertEqual(type(actual), int)
