#!/usr/bin/python3
"""File Storage Module"""

import json
from models.place import Place
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.state import State
from models.review import Review

class FileStorage():
    """
    FileStorage Class:
    Handles serialization and deserialization of objects to and from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all stored objects.
        Returns:
        dict: Dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the storage.
        Args:
        -----
        obj: Instance of a class derived from BaseModel.
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Save serialized objects to a JSON file.
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(self.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """
        Load serialized objects from a JSON file.
        """
        try:
            with open(self.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
