#!/usr/bin/python3
"""Entry point script for your application"""

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()

# Reload data into the storage instance
storage.reload()
