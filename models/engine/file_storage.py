#!/usr/bin/python3
"""
Module for FileStorage class
"""
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """
    serializes  and deserializes instances to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        """
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serialize __objects to de JSON file
        """
        j_objects = {}
        for key, values in FileStorage.__objects.items():
            j_objects[key] = values.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(j_objects, file)

    def reload(self):
        """
        deserialize the JSON file to __objects
        """

        if os.path.isfile(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as my_file:
                data = json.loads(my_file.read())
                for key, values in data.items():
                    str_dic = eval(values['__class__'])(**values)
                    FileStorage.__objects[key] = str_dic
