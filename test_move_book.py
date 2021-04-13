import io
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

    @patch('books.main_menu_selection')
    @patch('books.shelf_input_retry_and_convert')
    @patch('books.input_error_retry')
    @patch('builtins.input')
    @patch('books.move_book_no_result_retry')
    @patch('books.search_book')
    def test_move_book_input_error_retry_called(self, mock_search_book, mock_move_book_no_result_retry,
                                                mock_input, mock_input_error_retry,
                                                mock_shelf_input_retry_and_convert, mock_main_menu_selection):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")
        book_collection_list = [book_1]
        user_input = mock_input()
        verify_filtered_list = mock_move_book_no_result_retry()
        move_book(book_collection_list)
        mock_input_error_retry.assert_called_with(user_input, verify_filtered_list)

    @patch('books.main_menu_selection')
    @patch('books.shelf_input_retry_and_convert', return_value=None)
    @patch('books.input_error_retry')
    @patch('builtins.input', side_effect=["1", "1"])
    @patch('books.move_book_no_result_retry',
           return_value=[Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")])
    @patch('books.search_book')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_selected_book_print_string(self, mock_output, mock_search_book, mock_move_book_no_result_retry,
                                             mock_input, mock_input_error_retry,
                                             mock_shelf_input_retry_and_convert, mock_main_menu_selection):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", "9", "science", "computer")
        book_collection_list = [book_1]
        move_book(book_collection_list)
        selected_book = book_1
        str = mock_output.getvalue()
        str_split = str.split('\n')[0:3]
        actual = "".join(str_split)
        expected = f'You have selected >>> {selected_book}Which shelf do you want to move the book to? See options ' \
                   f'below: '
        self.assertEqual(actual, expected)

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
