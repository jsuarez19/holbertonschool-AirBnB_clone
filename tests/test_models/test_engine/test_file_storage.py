#!/usr/bin/python3
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_all(self):
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)
        self.assertIsEqual(storage.all(), storage.__objects)

    def test_reload(self):
        obj = BaseModel()
        storage = FileStorage()
        if os.path.exists(storage.__file_path):
            os.remove(storage.__file_path)
        storage.new(obj)
        storage.reload()
        self.assertEqual(len(storage.all()), 1)

    def test_new(self):
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        self.assertEqual(storage.all(), {"{}.\
{}".format(obj.__class__.__name, obj.id): obj})

    def test_save(self):
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))


if __name__ == "__main__":
    unittest.main()
