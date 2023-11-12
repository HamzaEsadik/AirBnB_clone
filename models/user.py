#!/usr/bin/python3
'''Defines the User class, which inherits from BaseModel.'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Represents the User class.'''

    email = ""  # User's email address
    password = ""  # User's password
    first_name = ""  # User's first name
    last_name = ""  # User's last name
