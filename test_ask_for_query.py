from unittest import TestCase
from unittest.mock import patch
from books import ask_for_query


class TestAskForQuery(TestCase):

    @patch('builtins.input', side_effect=["", "poland"])
    def test_ask_for_query_re_enter_input_called(self, mock_input):
        ask_for_query("author")
        mock_input.assert_called_with(f'Invalid entry, enter the author you want to search: ')

    @patch('builtins.input', side_effect=["", "ham"])
    def test_ask_for_query_return_string(self, mock_output):
        actual = ask_for_query("title")
        self.assertEqual(type(actual), str)
