from unittest import TestCase
from book import Book
from books import create_book_object


class TestCreateBookObject(TestCase):
    def test_create_book_object_check_list_has_book_object(self):
        json_string = """
        {
            "0": {
                "Author": "Ambroziak",
                "Title": "Michael Graves Images of a Grand Tour",
                "Publisher": "Princeton Architectural Press",
                "Shelf": 1,
                "Category": "Architecture",
                "Subject": "Architectural History"
            },
            "1": {
                "Author": "Lambert",
                "Title": "Building Seagram",
                "Publisher": "Yale",
                "Shelf": 1,
                "Category": "Architecture",
                "Subject": "Architectural History"
            }
        }
        """
        actual = create_book_object(json_string)
        for book in actual:
            self.assertIsInstance(book, Book)

    def test_create_book_object_return_list(self):
        json_string = """
        {
            "0": {
                "Author": "Ambroziak",
                "Title": "Michael Graves Images of a Grand Tour",
                "Publisher": "Princeton Architectural Press",
                "Shelf": 1,
                "Category": "Architecture",
                "Subject": "Architectural History"
            }
        }
        """
        actual = create_book_object(json_string)
        self.assertEqual(type(actual), list)
