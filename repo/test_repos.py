from unittest import TestCase
from unittest.mock import MagicMock

from db_client.client_elasticsearch import ClientES
from repo.repos import Repo


class TestRepo(TestCase):

    def setUp(self) -> None:
        self.client = ClientES()
        self.repo = Repo(self.client)
        self.repo.get_tweet = MagicMock(return_value={
            "query":
                {"match_all": {}},
            "size": 20,
            "from": 0
        })

    def test_init_(self):
        self.assertIsInstance(self.repo, Repo)

    def test_get_tweet(self):
        expected_result = {
            "query":
                {"match_all": {}},
            "size": 20,
            "from": 0
        }
        res = self.repo.get_tweet(index_name='index_name')
        self.assertEqual(res, expected_result)
