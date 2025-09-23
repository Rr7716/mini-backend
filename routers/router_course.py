from typing import List
from bson import ObjectId
from fastapi import APIRouter, FastAPI, HTTPException
from configrations import db
from models.course import Course

router = APIRouter()

collection = db['course']

@router.get("/", response_model=List[Course])
async def get_all_course_time():
    cursor = collection.find({'belong_week': 1, 'is_delete': False})
    data = []
    i = 0
    for doc in cursor:
        data.append(Course(**doc))
        data[i].id = str(doc['_id'])
        i+=1
    return data

@router.post("/")
async def create_course(new_course :Course):
    try:
        print(new_course)
        resp = collection.insert_one(new_course.model_dump())
        return {"status_code":200, "id":str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

@router.put("/{course_id}")
async def update_course(course_id:str, updated_course:Course):
    try:
        id = ObjectId(course_id)
        exesting_doc = collection.find_one({"_id":id, "is_delete":False})
        if not exesting_doc:
            return HTTPException(status_code=404, detail=f"Course does not exits")
        resp = collection.update_one({"_id":id}, {"$set":dict(updated_course)})
        return {"status_code":200, "message": "Course Updated Successfully"}
 
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")
 
@router.delete("/{course_id}")
async def delete_course(course_id:str):
    try:
        id = ObjectId(course_id)
        exesting_doc = collection.find_one({"_id":id, "is_delete":False})
        if not exesting_doc:
            return HTTPException(status_code=404, detail=f"Course does not exits")
        resp = collection.update_one({"_id":id}, {"$set":{"is_delete":True}})
        return {"status_code":200, "message": "Course Deleted Successfully"}
 
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")