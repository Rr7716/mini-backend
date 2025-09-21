from typing import List
from fastapi import APIRouter, FastAPI, HTTPException
from configrations import db
from models.course_time import CourseTime

router = APIRouter()

@router.get("/", response_model=List[CourseTime])
async def get_all_course_time():
    cursor = db['course_time'].find()
    data = []
    i = 0
    for doc in cursor:
        data.append(CourseTime(**doc))
        data[i].id = str(doc['_id'])
        i+=1
    return data

@router.post("/")
async def create_course_time(new_course_time :CourseTime):
    try:
        print(new_course_time)
        resp = db['course_time'].insert_one(new_course_time.model_dump())
        return {"status_code":200, "id":str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

