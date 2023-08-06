#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_init(self):
        obj = Amenity()
        self.assertEqual(obj.name, "")


if __name__ == "__main__":
    unittest.main()
