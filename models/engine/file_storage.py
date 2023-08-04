#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["{}.\
{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Writes dict __objects to a JSON file"""
        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as f:
            dictionary = {}
            for k,v in FileStorage.__objects.items():
                dictionary[k] = v.to_dict()
            f.write(json.dumps(dictionary))

    def reload(self):
        """Reads JSON file"""
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, mode='r', encoding="utf-8") as f:
                read_data = f.read()
                dictionary = json.loads(read_data)
                for k, v in dictionary.items():
                    value = dictionary[k]
                    obj = eval(value['__class__'])(**value)
                    FileStorage.__objects[k] = obj
        else:
            pass
