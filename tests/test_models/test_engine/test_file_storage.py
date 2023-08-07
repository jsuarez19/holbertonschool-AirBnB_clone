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

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all(self):
        storage = FileStorage()
        obj = storage.all()
        self.assertIsInstance(obj, dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_reload(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        storage.reload()
        self.assertEqual(len(storage.all()), 2)

    def test_new(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        self.assertEqual(storage.all(), {"{}.\
{}".format(obj.__class__.__name__, obj.id): obj})
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save(self):
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))


if __name__ == "__main__":
    unittest.main()
