#!/usr/bin/python3

import json
import os


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        self.__objects["{}.\
{}".format(obj.__class__.__name__, obj.id)] = obj.to_dict()

    def save(self):
        """Writes dict __objects to a JSON file"""
        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            json_str = json.dumps(self.__objects)
            f.write(json_str)

    def reload(self):
        """Reads JSON file"""
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, mode='r', encoding="utf-8") as f:
                read_data = f.read()
                dictionary = json.loads(read_data)
                for k, v in dictionary.items():
                    value = dictionary[k]
                    obj = eval(value['__class__'])(**value)
                    self.__objects[k] = obj
        else:
            pass
