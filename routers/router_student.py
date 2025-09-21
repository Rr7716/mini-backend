from typing import List
from fastapi import APIRouter, FastAPI, HTTPException
from configrations import db
from models.student import Student

router = APIRouter()

@router.get("/", response_model=List[Student])
async def get_all_course_time():
    cursor = db['student'].find()
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
        resp = db['student'].insert_one(new_student.model_dump())
        return {"status_code":200, "id":str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

