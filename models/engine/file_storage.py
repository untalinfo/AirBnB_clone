#!/usr/bin/python3
import json
import os
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        id = obj.id
        FileStorage.__objects['id'] = id

    def save(self):
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
         if os.path.isfile(FileStorage.__file_path):
             with open(FileStorage.__file_path) as my_file:
                 my_dic = json.load(my_file)
                 for keys, value in my_dic:
                     FileStorage.__objects[keys] = value
         else:
             pass
     

    
