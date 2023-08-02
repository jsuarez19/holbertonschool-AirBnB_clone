#!/usr/bin/python3

import json
import os


class FileStorage:

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

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
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding="utf-8") as f:
                read_data = f.read()
            self.__objects = json.loads(read_data)
        else:
            pass
