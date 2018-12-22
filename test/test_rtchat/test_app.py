from unittest import TestCase

from rtchat.apps import RtchatConfig


class TestUtils(TestCase):

    def setUp(self):
        self.app = RtchatConfig("rtchat", "rtchat")

