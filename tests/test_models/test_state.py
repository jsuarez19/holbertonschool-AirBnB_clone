#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_init(self):
        obj = State()
        self.assertEqual(obj.name, "")


if __name__ == "__main__":
    unittest.main()
