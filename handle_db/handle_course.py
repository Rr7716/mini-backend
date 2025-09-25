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
        