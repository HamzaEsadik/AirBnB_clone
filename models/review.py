#!/usr/bin/python3
'''Review Class - Inheritance from BaseModel'''
from models.base_model import BaseModel

class Review(BaseModel):
    '''Review Class - Represents a review'''

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes Review instance"""
        super().__init__(*args, **kwargs)
