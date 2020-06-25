#!/usr/bin/python3
"""
Module Classe base for airbnb
"""
import uuid
import datetime


class BaseModel:
    """
    This class defines attributes or methods for
    other classes
    """
    name = None
    my_number = 0

    def __init__(self):
        """
        Initialize of base model class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        crate a string

        Returns:
            [str]: [Unofficial string]
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance updated_at to current
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Generate a dictionary of the class
        """
        dic = {}
        dic["__class__"] = str(type(self).__name__)
        dic['id'] = self.id
        dic["my_number"] = self.my_number
        dic["name"] = self.name
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        return dic
