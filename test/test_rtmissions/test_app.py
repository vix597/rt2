from unittest import TestCase

from rtmissions.apps import RtmissionsConfig


class TestUtils(TestCase):

    def setUp(self):
        self.app = RtmissionsConfig("rtmissions", "rtmissions")

