from unittest import TestCase

from rtwiki.apps import RtwikiConfig


class TestUtils(TestCase):

    def setUp(self):
        self.app = RtwikiConfig("rtwiki", "rtwiki")

