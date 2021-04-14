from unittest import TestCase
from unittest.mock import patch
from books import convert_excel_to_json, EXCEL_FILENAME
import pandas


class TestConvertExcelToJson(TestCase):

    @patch('books.write_dictionary_to_file')
    @patch('pandas.read_excel', return_value=pandas.DataFrame())
    def test_convert_excel_to_json_write_dictionary_to_file_called(self, mock_read_excel,
                                                                   mock_write_dictionary_to_file):
        convert_excel_to_json(EXCEL_FILENAME())
        converted_json = "{\n\n}"
        mock_write_dictionary_to_file.assert_called_once_with(converted_json)

    def test_convert_excel_to_json_return_list(self):
        actual = convert_excel_to_json(EXCEL_FILENAME())
        self.assertEqual(type(actual), list)
