from datetime import datetime
from typing import List
from fastapi import APIRouter, FastAPI, HTTPException
from configrations import db
from handle_db.handle_course import get_by_id
from handle_db.handle_removetimes import get
from models.removetimes import RemoveTimes
from fastapi import APIRouter, WebSocket, WebSocketDisconnect


collection = db['removetimes']

router = APIRouter()
@router.get("/")
async def get_all():
    records= []
    data = get()
    for one in data:
        course = get_by_id(one.course_id)[0]
        records.append({
            'content': course.content,
            'weekday': course.weekday,
            'timerange': f'{course.course_time.start_time}-{course.course_time.end_time}',
            'students': " ".join([s.en_name for s in course.students]),
            'course_left': course.course_left,
            'create_time': one.create_time,
        })
