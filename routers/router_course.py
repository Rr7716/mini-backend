from typing import List
from fastapi import APIRouter, FastAPI, HTTPException
from configrations import db
from models.course import Course

router = APIRouter()

@router.get("/", response_model=List[Course])
async def get_all_course_time():
    cursor = db['course'].find()
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
        resp = db['course'].insert_one(new_course.model_dump())
        return {"status_code":200, "id":str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

