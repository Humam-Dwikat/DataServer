from unittest import TestCase

from confing.configDB import Config


class TestConfig(TestCase):

    def test_init_(self):
        with self.assertRaises(Exception):
            _ = Config()

    def test_get_instance(self):
        object1 = Config.get_instance()
        self.assertIsInstance(object1, Config)
