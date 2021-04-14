import io
from unittest import TestCase
from unittest.mock import patch
from books import choice_validate


class TestChoiceValidate(TestCase):

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choice_validate_print_choice_list(self, mock_output, mock_input):
        option_list = ["Search", "Move", "Quit"]
        choice_validate(option_list)
        expected = "1. Search\n2. Move\n3. Quit\n"
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('builtins.input', side_effect=["5", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choice_validate_incorrect_input_retry(self, mock_output, mock_input):
        option_list = ["Search", "Move", "Quit"]
        choice_validate(option_list)
        expected = "1. Search\n2. Move\n3. Quit\nInput is not an option, please try again.\n"
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('builtins.input', return_value="2")
    def test_choice_validate_return_string(self, mock_input):
        option_list = ["Search", "Move", "Quit"]
        actual = choice_validate(option_list)
        self.assertEqual(type(actual), str)
