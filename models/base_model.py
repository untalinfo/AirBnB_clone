#!/usr/bin/python3
"""
Module Classe base for airbnb
"""
import uuid
from datetime import datetime


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
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
