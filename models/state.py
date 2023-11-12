#!/usr/bin/python3
'''State Class - Inheritance from BaseModel'''
from models.base_model import BaseModel


class State(BaseModel):
    '''State Class - Represents a state'''

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes State instance"""
        super().__init__(*args, **kwargs)
