#!/usr/bin/python3
import json
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
                 FileStorage.__objects = cls.from_json_string(my_file.read())
         else:
             pass
     

    
