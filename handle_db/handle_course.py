from bson import ObjectId
from configrations import db
from models.course import Course
from public.ser import to_serializable

collection = db['course']

def update_course(id: ObjectId, updated_course:dict):
    try:
        exesting_doc = collection.find_one({"_id":id, "is_delete":False})
        if not exesting_doc:
            return False, 'Course does not exits'
        collection.update_one({"_id":id}, {"$set": updated_course})
        return True, ''
    except Exception as e:
        return True, f'Some error occured {e}'

def get_by_id(course_id: str):
    cursor = collection.find({
        "_id": ObjectId(course_id),
    })
    return format(cursor)

def format(cursor):
    data = []
    for doc in cursor:
        course = Course(**doc)
        course.id = str(doc['_id'])
        data.append(course)
    return data