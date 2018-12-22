from unittest import TestCase

from rthosts.apps import RthostsConfig


class TestUtils(TestCase):

    def setUp(self):
        self.app = RthostsConfig("rthosts", "rthosts")

