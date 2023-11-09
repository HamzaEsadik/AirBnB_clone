#!/usr/bin/env bash
'''Base Model'''
import uuid
from datetime import datetime
class BaseModel:
    '''Base model class'''
    def __init__(self):
        '''the init method'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''str method'''
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        '''update update_at with current time'''
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return new_dict
