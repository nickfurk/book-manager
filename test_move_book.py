from unittest import TestCase
from unittest.mock import patch
from books import move_book
from book import Book


class TestMoveBook(TestCase):

    @patch('books.main_menu_selection')
    @patch('books.shelf_input_retry_and_convert')
    @patch('books.input_error_retry')
    @patch('builtins.input', side_effect=[None, '1'])
    @patch('books.search_book')
    def test_move_book_search_book_called(self, mock_search_book, mock_input, mock_input_error_retry,
                                          mock_shelf_input_retry_and_convert, mock_main_menu_selection):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")
        book_collection_list = [book_1]
        move_book(book_collection_list)
        mock_search_book.assert_called_with(book_collection_list)

    @patch('books.main_menu_selection')
    @patch('books.shelf_input_retry_and_convert')
    @patch('books.input_error_retry')
    @patch('builtins.input', side_effect=[None, '1'])
    @patch('books.move_book_no_result_retry')
    @patch('books.search_book')
    def test_move_book_move_book_no_result_retry_called(self, mock_search_book, mock_move_book_no_result_retry,
                                                        mock_input, mock_input_error_retry,
                                                        mock_shelf_input_retry_and_convert, mock_main_menu_selection):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")
        book_collection_list = [book_1]
        filtered_list = mock_search_book()
        move_book(book_collection_list)
        mock_move_book_no_result_retry.assert_called_with(filtered_list, book_collection_list)

    def test_move_book_verify_user_input_called(self):
        pass

    def test_move_selected_book_called(self):
        pass

    def test_move_selected_book_print_string(self):
        pass

    def test_move_shelf_options_called(self):
        pass

    def test_move_user_shelf_input_print_string(self):
        pass

    def test_move_verify_user_shelf_input_called(self):
        pass

    def test_move_selected_book_updates(self):
        pass

    def test_move_shelf_update_print_string(self):
        pass

    def test_move_main_menu_selection_called(self):
        pass
