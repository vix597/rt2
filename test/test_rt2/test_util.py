from unittest import TestCase
from unittest.mock import mock_open, patch

from rt2.util import get_secret_key

class TestUtils(TestCase):

    @patch("os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data="TESTING_KEY")
    def test_key_file_exists(self, mock_file, mock_exists):
        mock_exists.return_value = True
        self.assertEqual(get_secret_key("test/path"), "TESTING_KEY")

    @patch("os.path.exists")
    @patch("random.choice")
    @patch("builtins.open", new_callable=mock_open)
    def test_key_file_not_exists(self, mock_file, mock_choice, mock_exists):
        mock_exists.return_value = False
        mock_choice.return_value = "a"
        self.assertEqual(get_secret_key("test/path"), "a"*50)

