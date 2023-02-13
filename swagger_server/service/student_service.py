from pymongo import MongoClient

import os

# DB config and init
connectionString = os.getenv("MONGO_URI")
dbClient = MongoClient(connectionString)
db = dbClient["student"]
collection = db["info"]

unique_id = 0


def add(student=None):
    global unique_id
    student.student_id = unique_id

    collection.insert_one(student.to_dict())

    unique_id = unique_id + 1
    return unique_id - 1


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
