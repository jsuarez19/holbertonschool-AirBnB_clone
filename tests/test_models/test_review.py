#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_init(self):
        obj = Review()
        self.assertEqual(place_id, "")
        self.assertEqual(user_id, "")
        self.assertEqual(text, "")


if __name__ == "__main__":
    unittest.main()
