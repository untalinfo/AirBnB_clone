#!/usr/bin/python3
"""
Module for FileStorage class
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
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
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serialize __objects to de JSON file
        """
        j_objects = {}
        for key in FileStorage.__objects:
            j_objects[key] = FileStorage.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(j_objects, file)

    def reload(self):
        """
        deserialize the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as my_file:
                data = json.loads(my_file.read())
                for key, values in data.items():
                    FileStorage.__objects[key] = BaseModel(**values)
        else:
            pass
