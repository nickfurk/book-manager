import io
from unittest.mock import patch
from unittest import TestCase
from books import main_menu_selection


class TestMainMenuSelection(TestCase):

    @patch('books.main_menu_selection', return_value=None)
    @patch('books.choice_validate', return_value="1")
    @patch('books.search_book')
    def test_user_selects_option_1_search_book_is_called(self, mock_search_book, mock_choice_validate,
                                                         mock_main_menu_selection):
        mock_list = [1, 2, 3, 4, 5]
        main_menu_selection(mock_list)
        mock_search_book.assert_called_with(mock_list)

    @patch('books.main_menu_selection', return_value=None)
    @patch('books.search_book', return_value=None)
    @patch('books.choice_validate', return_value="1")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_selects_option_1_print_correct_string(self, mock_output, mock_choice_validate, mock_search_book,
                                                        mock_main_menu_selection):
        mock_list = [1, 2, 3, 4, 5]
        main_menu_selection(mock_list)
        expected = f'\nWhat would you like to do?\n\n\nWhat would like to search for?\n\n'
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('books.choice_validate', return_value="2")
    @patch('books.move_book')
    def test_user_selects_option_2_move_book_is_called(self, mock_move_book, mock_choice_validate):
        mock_list = [1, 2, 3, 4, 5]
        main_menu_selection(mock_list)
        mock_move_book.assert_called_with(mock_list)

    @patch('books.move_book')
    @patch('books.choice_validate', return_value="2")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_selects_option_1_print_correct_string(self, mock_output, mock_choice_validate, mock_move_book):
        mock_list = [1, 2, 3, 4, 5]
        main_menu_selection(mock_list)
        expected = f'\nWhat would you like to do?\n\n\nLet\'s find your desired book first, before we move it. Select ' \
                   f'an attribute.\n\n'
        self.assertEqual(mock_output.getvalue(), expected)

    @patch('books.choice_validate', return_value="3")
    @patch('books.save')
    def test_user_selects_option_3_save_is_called(self, mock_save, mock_choice_validate):
        mock_list = [1, 2, 3, 4, 5]
        main_menu_selection(mock_list)
        mock_save.assert_called_with(mock_list)
