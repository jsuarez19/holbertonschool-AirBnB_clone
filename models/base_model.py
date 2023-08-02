#!/usr/bin/python3
"""
Writing the BaseModel class
"""


from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Class BaseModel"""
    def __init__(self):
        """Constructor"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """__str__ method"""
        name = type(self).__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """Updates current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a new dictionary"""
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = str(self.created_at.isoformat())
        new_dict["updated_at"] = str(self.updated_at.isoformat())
        return new_dict
