#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_str(self):
        obj = BaseModel()
        obj_str = str(obj)
        out_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(obj_str, out_str)

    def test_save(self):
        obj = BaseModel()
        first_crt = obj.created_at
        first_upd = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, datetime.utcnow())
        second_crt = obj.created_at
        second_upd = obj.updated_at
        self.assertEqual(first_crt, second_crt)
        self.assertNotEqual(first_upd, second_upd)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)


    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()
