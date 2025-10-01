from datetime import datetime
from typing import List
from fastapi import APIRouter, FastAPI, HTTPException
from configrations import db
from handle_db.handle_takeleave import get_by_range
from models.takeleave import TakeLeave
from handle_db.handle_course import update_course as update
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from public.time_tools import get_week_range

collection = db['takeleave']
router = APIRouter()

@router.get("/{course_id}", response_model=List[TakeLeave])
async def get_takeleave(course_id:str):
    cursor = collection.find({'course_id': course_id})
    data = []
    for doc in cursor:
        takeleave = TakeLeave(**doc)
        takeleave.id = str(doc['_id'])
        data.append(takeleave)
    return data

@router.get("/range", response_model=List[TakeLeave])
async def get_takeleave_by_range():
    monday_str, sunday_str = get_week_range()
    return get_by_range(monday_str, sunday_str)

@router.post("/")
async def create_takeleave(new_takeleave :TakeLeave):
    try:
        new_takeleave.create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(new_takeleave)
        resp = collection.insert_one(new_takeleave.model_dump())
        return {"status_code":200, "id":str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")