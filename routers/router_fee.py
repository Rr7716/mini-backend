from typing import List
from fastapi import APIRouter, FastAPI, HTTPException
from configrations import db
from models.fee import Fee

router = APIRouter()

@router.get("/", response_model=List[Fee])
async def get_all_course_time():
    cursor = db['fee'].find()
    data = []
    i = 0
    for doc in cursor:
        data.append(Fee(**doc))
        data[i].id = str(doc['_id'])
        i+=1
    return data

@router.post("/")
async def create_fee(new_fee :Fee):
    try:
        print(new_fee)
        resp = db['fee'].insert_one(new_fee.model_dump())
        return {"status_code":200, "id":str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

