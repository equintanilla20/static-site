import unittest
from main import *


class TestMain(unittest.TestCase):
    def test_extract_title_01(self):
        title = extract_title("# This is a heading")
        self.assertEqual(title, "This is a heading")


if __name__ == '__main__':
    unittest.main()
