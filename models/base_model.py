#!/usr/bin/python3
"""
Writing the BaseModel class
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        if kwargs != {}:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
                if k == "updated_at":
                    self.updated_at = datetime.strptime(v, '%Y-%m-\
%dT%H:%M:%S.%f')
                if k == "created_at":
                    self.created_at = datetime.strptime(v, '%Y-%m-\
%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """__str__ method"""
        name = type(self).__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """Updates current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns a new dictionary"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = str(self.created_at.isoformat())
        new_dict["updated_at"] = str(self.updated_at.isoformat())
        return new_dict
