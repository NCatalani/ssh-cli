import json

from enum import Enum
from typing import Any

class CLICategory(str, Enum):
    CONNECTION = "Connection"
    FOLDER = "Folder"
    COLLECTION = "Collection"


class CLIEntity(object):
    __name: str
    __category: "CLICategory"
    __value: Any

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def value(self):
        return self.__value

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name is not a string! %s" % type(name))

        self.__name = name

    @category.setter
    def category(self, category):
        if not isinstance(category, CLICategory):
            raise TypeError("Category is not a CLICategory! %s" % type(category))

        self.__category = category

    @value.setter
    def value(self, value=None):
        self.__value = value

    def __init__(self, name, category, value=None):
        self.name = name
        self.category = category
        self.value = value

    def __repr__(self):
        return json.dumps(self.serialize())

    def __serialize_element(self, e):

        if isinstance(e, CLIEntity):
            return e.serialize()
        elif isinstance(e, list):
            return [ self.__serialize_element(se) for se in e ]

        return e

    def serialize(self):
        return {
            "name": self.name,
            "category": self.category.value,
            "value": self.__serialize_element(self.value)
        }

