#!/usr/bin/python3
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_all(self):
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)
        self.assertIsEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        storage.reload()
        self.assertEqual(len(storage.all()), 2)

    def test_new(self):
        obj = BaseModel()
        storage = FileStorage()
        storage.new(obj)
        self.assertEqual(storage.all(), {"BaseModel.{}".format(obj.id): obj})

    def test_save(self):
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    
if __name__ == "__main__":
    unittest.main()
