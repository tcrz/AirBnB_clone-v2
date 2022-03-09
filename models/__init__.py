#!/usr/bin/python3
"""This module instantiates an object of class FileStorage/ DBstorage"""
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBstorage
    storage = DBstorage()
    storage.reload()
    # print("DB mode")
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
# print("FILE mode")
