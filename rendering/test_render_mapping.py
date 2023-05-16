import json
from unittest import TestCase
from unittest.mock import patch, mock_open

from rendering.render_mapping import read_file, render_mapping


class TestRenderMapping(TestCase):
    """test for render_mapping and read_file """
    def test_read_file(self):
        content_file = """{
                "mappings": {
                "dynamic": true,
                "properties": {
                    "text": {
                        "type":"text"
                        }
                    }}
                   """
        with patch('builtins.open', mock_open(read_data=content_file)):
            result = read_file('fake_path')
            self.assertEqual(result, content_file)

        with self.assertRaises(OSError):
            file = read_file("fake/path")

    def test_render_mapping(self):
        expected_result = """{
                              "mappings": {
                                "dynamic": true,
                                "properties": {
                                    "coordinates": {
                                        "type": "geo_point"
                                        }
                                  }
                              },
                              "settings": {
                                "number_of_replicas": 1,
                                "number_of_shards": 2
                              }
                            }
                        """
        expected_settings = {'number_of_replicas': 1, 'number_of_shards': 2}

        def reader(path: str) -> str:
            return expected_result

        result = render_mapping(
            path='fake_path',
            number_of_replicas=1,
            number_of_shards=2,
            render=reader)
        settings = result['settings']
        self.assertEqual(settings, expected_settings)

        def wrong_reader(path: str) -> str:
            return """{
                              "mappings": {
                                "dynamic": true,
                                "properties": {
                                    'coordinates": {
                                        "type": "geo_point"
                                        }
                                  }
                              """

        with self.assertRaises(json.JSONDecodeError):
            _ = result = render_mapping(
                path='fake_path',
                number_of_replicas=1,
                number_of_shards=2,
                render=wrong_reader)
