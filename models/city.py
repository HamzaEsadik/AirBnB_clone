#!/usr/bin/python3
'''class inherent of BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''city class'''

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes City"""
        super().__init__(*args, **kwargs)
