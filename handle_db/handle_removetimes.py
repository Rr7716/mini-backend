from datetime import datetime
from bson import ObjectId
from configrations import db
from models.removetimes import RemoveTimes

collection = db['removetimes']

def get():
    cursor = collection.find()
    return format(cursor)


def insert_removetimes(new: RemoveTimes):
    new.create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(new)
    collection.insert_one(new.model_dump())


def format(cursor):
    data = []
    for doc in cursor:
        removetimes = RemoveTimes(**doc)
        removetimes.id = str(doc['_id'])
        data.append(removetimes)
    return data