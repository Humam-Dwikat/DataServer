from unittest import TestCase
from unittest.mock import patch, mock_open

from libs.handler import read_file_line_by_line, stream


class TestOperationES(TestCase):
    """
    This is a simple unittest
    """
    def test_index_document(self):
        pass

    def test_read_file_line_by_line(self):
        """
        want to test if the function return the generator
        """
        expected_result = yield """'key1': 'value1', 'key2': 'value2'}"""
        with patch('builtins.open', mock_open(read_data=expected_result)):
            result = read_file_line_by_line('fake_path')
            self.assertEqual(result, expected_result)

    def test_stream(self):
        expected_result = yield """
                            {'_op_type': 'index','_index': 'index_name',
                            '_id': '12345',
                            '_source': '{"id_str": 
                            "12345", "text": "This is a tweet"}'} 
                            """

        with patch('handler.read_file_line_by_line',
                   mock_open(read_data=expected_result)):
            result = stream('fake_path', 'index_name')
            self.assertEqual(result, expected_result)
