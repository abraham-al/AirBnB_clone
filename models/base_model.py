#!/usr/bin/python3
"""File containing BaseModel Class"""

from datetime import datetime
import models
import uuid


class BaseModel:

    def __init__(self, *args, **kwargs):
        """Initialize a new Base Model"""
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime\
                        .strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                elif key == "id":
                    self.id = value
                elif key == "__class__":
                    self.__class__.__name__ = kwargs[key]
                else:
                    setattr(self, key, value)

    def __str__(self):
        """String representation of the Base Model"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current time"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary of BaseModel"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = datetime.isoformat(self.created_at)
        my_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return my_dict
