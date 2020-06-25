#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    name = None
    my_number = 0
    id = None

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dic = {}
        dic["__class__"] = str(type(self).__name__)
        dic['id'] = self.id
        dic["my_number"] = self.my_number
        dic["name"] = self.name
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        return dic
