from typing import List
from bson import ObjectId
from fastapi import APIRouter, FastAPI, HTTPException
from configrations import db
from models.student import Student

router = APIRouter()

collection = db['student']

@router.get("/", response_model=List[Student])
async def get_all_course_time():
    cursor = collection.find({'is_delete': False})
    data = []
    i = 0
    for doc in cursor:
        data.append(Student(**doc))
        data[i].id = str(doc['_id'])
        i+=1
    return data

@router.post("/")
async def create_student(new_student :Student):
    try:
        print(new_student)
        resp = collection.insert_one(new_student.model_dump())
        return {"status_code":200, "id":str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

@router.delete("/{student_id}")
async def delete_student(student_id:str):
    try:
        id = ObjectId(student_id)
        exesting_doc = collection.find_one({"_id":id, "is_delete":False})
        if not exesting_doc:
            return HTTPException(status_code=404, detail=f"Course does not exits")
        resp = collection.update_one({"_id":id}, {"$set":{"is_delete":True}})
        return {"status_code":200, "message": "Course Deleted Successfully"}
 
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")