from unittest import TestCase
from books import check_if_shelf_category


class TestCheckIfShelfCategory(TestCase):

    def test_check_if_shelf_category_change_user_query_to_int(self):
        category = "shelf"
        user_query = "1"
        actual = check_if_shelf_category(category, user_query)
        self.assertEqual(actual, 1)

    def test_check_if_shelf_category_change_user_query_to_title_string(self):
        category = "shelf"
        user_query = "gaby"
        actual = check_if_shelf_category(category, user_query)
        self.assertEqual(actual, "Gaby")
