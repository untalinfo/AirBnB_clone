#!/usr/bin/python3
"""
Module Classe base for airbnb
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    This class defines attributes or methods for
    other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize of base model class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

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
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Generate a dictionary of the class
        """
        dic = {}
        dic["__class__"] = str(type(self).__name__)
        dic['id'] = self.id
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        return dic
