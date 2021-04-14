from unittest import TestCase
from unittest.mock import patch
from books import find_query
from book import Book


class TestFindQuery(TestCase):

    @patch('books.check_if_shelf_category')
    def test_find_query_check_if_shelf_category_called(self, mock_check_if_shelf_category):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", 1, "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", 1, "math", "matrix")
        book_collection = [book_1, book_2]
        user_query = "1"
        user_menu_choice_category = "shelf"
        find_query(book_collection, user_query, user_menu_choice_category)
        mock_check_if_shelf_category.assert_called_with("shelf", user_query)

    def test_find_query_return_filtered_list_non_shelf(self):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", 1, "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", 1, "math", "matrix")
        book_collection = [book_1, book_2]
        user_query = "lip"
        user_menu_choice_category = "author"
        actual = find_query(book_collection, user_query, user_menu_choice_category)
        expected = [book_2]
        self.assertEqual(actual, expected)

    def test_find_query_return_filtered_list_shelf(self):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", 4, "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", 1, "math", "matrix")
        book_collection = [book_1, book_2]
        user_query = "1"
        user_menu_choice_category = "shelf"
        actual = find_query(book_collection, user_query, user_menu_choice_category)
        expected = [book_2]
        self.assertEqual(actual, expected)

    def test_find_query_return_list_type(self):
        book_1 = Book("123", "April C", "Hacking with April", "Chris", 1, "science", "computer")
        book_2 = Book("456", "Lipra", "Coding with April", "Johnson", 1, "math", "matrix")
        book_collection = [book_1, book_2]
        user_query = "Chr"
        user_menu_choice_category = "publisher"
        actual = find_query(book_collection, user_query, user_menu_choice_category)
        self.assertEqual(type(actual), list)
