#!/usr/bin/python3
'''City Class - Inheritance from BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''City Class - Represents a city'''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes City instance"""
        super().__init__(*args, **kwargs)
