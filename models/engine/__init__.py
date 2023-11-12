#!/usr/bin/python3
'''Application FileStorage Configuration'''
from models.engine.file_storage import FileStorage

'''Create a unique FileStorage instance for the application'''
storage = FileStorage()

'''Reload data into the storage instance'''
storage.reload()
