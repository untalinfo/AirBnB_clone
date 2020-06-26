#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
class FileStorage:
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):

        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        j_objects = {}
        for key in FileStorage.__objects:
            j_objects[key] = FileStorage.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(j_objects, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r+') as my_file:
                data = json.loads(my_file.read())
                for key, values in data.items():
                    FileStorage.__objects[key] = BaseModel(**values)
        except:
            pass
