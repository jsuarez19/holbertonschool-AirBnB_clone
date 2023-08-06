#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_init(self):
        obj = User()
        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")


if __name__ == "__main__":
    unittest.main()
