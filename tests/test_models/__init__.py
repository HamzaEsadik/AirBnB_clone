#!/usr/bin/python3
"""Application-specific FileStorage Instance"""

# Importing the FileStorage class from the engine module
from models.engine.file_storage import FileStorage

# Creating a unique FileStorage instance for the application
storage = FileStorage()

# Reloading data from the storage file (if any)
storage.reload()
