import json
import os
import tempfile
from functools import reduce

from tinydb import TinyDB, Query
from pymongo import MongoClient

db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "students.json")
student_db = TinyDB(db_file_path)

# DB config and init
connectionString = "mongodb://root:verysecure@127.0.0.1:27017/devopscloud?authSource=admin"
dbClient = MongoClient(connectionString)
db = dbClient["student"]
collection = db["info"]


def add(student=None):
    collection.insert_one(student.to_dict())
    return student.student_id


def get_by_id(student_id=None, subject=None):
    student = collection.find_one({'student_id': student_id})
    if not student:
        return 'not found', 404

    student.pop("_id")
    return student


def delete(student_id=None):
    student = collection.find_one_and_delete({'student_id': student_id})
    if not student:
        return 'not found', 404
    return student_id
