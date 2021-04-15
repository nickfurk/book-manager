from unittest import TestCase
from books import change_none_to_string


class TestChangeNoneToString(TestCase):

    def test_change_none_to_string(self):
        somebook_dict = {
            "0": {
                "Author": "Langly",
                "Title": "The Road Less Travelled",
                "Publisher": None,
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
            }}
        actual = change_none_to_string(somebook_dict)
        expected = {
            "0": {
                "Author": "Langly",
                "Title": "The Road Less Travelled",
                "Publisher": "None",
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
            }}
        self.assertEqual(actual, expected)

    def test_change_none_to_string_return_dictionary(self):
        somebook_dict = {
            "0": {
                "Author": "Langly",
                "Title": "The Road Less Travelled",
                "Publisher": None,
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
            }}
        actual = change_none_to_string(somebook_dict)
        self.assertEqual(type(actual), dict)
