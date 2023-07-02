from unittest import TestCase

from db_client.client_elasticsearch import ClientES


class TestRepo(TestCase):

    def setUp(self) -> None:
        self.client = ClientES()

    def test_init_(self):
        self.assertIsInstance(self.client, ClientES)

    def test_get_tweet(self):
        self.fail()
