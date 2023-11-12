#!/usr/bin/python3
'''Amenity Class - Inheritance from BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Amenity Class - Represents an amenity'''
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity instance"""
        super().__init__(*args, **kwargs)
