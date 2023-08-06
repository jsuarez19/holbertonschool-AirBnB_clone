#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_init(self):
        obj = City()
        self.assertEqual(obj.state_id, "")
        self.assertEqual(obj.name, "")


if __name__ == "__main__":
    unittest.main()
