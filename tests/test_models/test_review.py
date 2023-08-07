#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_init(self):
        obj = Review()
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.text, "")


if __name__ == "__main__":
    unittest.main()
