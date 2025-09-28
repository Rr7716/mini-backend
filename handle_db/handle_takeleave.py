from bson import ObjectId
from configrations import db
from models.takeleave import TakeLeave

collection = db['takeleave']

def get(course_id: str, start_time, end_time):
    cursor = collection.find({
        "course_id": course_id,
        "create_time": {
            "$gte": start_time,
            "$lte": end_time
        }
    })
    return format(cursor)

def get_by_range(start_time, end_time):
    cursor = collection.find({
        "create_time": {
            "$gte": start_time,
            "$lte": end_time
        }
    })
    return format(cursor)

def format(cursor):
    data = []
    for doc in cursor:
        takeleave = TakeLeave(**doc)
        takeleave.id = str(doc['_id'])
        data.append(takeleave)
    return data