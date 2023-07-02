from unittest import TestCase

from elasticsearch import Elasticsearch

from db_client.client_elasticsearch import ClientES


class TestClientES(TestCase):
    def setUp(self):
        self.client = ClientES()

    def test__init__(self):
        self.assertEqual(self.client.db_host, 'localhost')

    def test_get_client(self):
        object1 = self.client.get_client()
        self.assertIsInstance(object1, Elasticsearch)
