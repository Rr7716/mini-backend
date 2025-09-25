from datetime import datetime
import json
from typing import List
from bson import ObjectId
from fastapi import APIRouter, FastAPI, HTTPException
from configrations import db
from models.course import Course
from public.ser import to_serializable
from handle_db.handle_course import update_course as update
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from websocket_manager import ConnectionManager

collection = db['course']

router_ws = APIRouter()
manager = ConnectionManager()

@router_ws.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # 这里只是回显，可以改成你需要的逻辑
            await manager.send_personal_message(f"你发了: {data}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)


# 自动消课时
async def autp_expire():
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S') # 2025-09-25 13:37:34
    date = now_str.split(' ')[0] # 2025-09-25
    today = datetime.today()
    weekday = today.isoweekday() # 1-7
    cursor = collection.find({'belong_week': 1, 'is_delete': False})
    for doc in cursor:
        course = Course(**doc)
        course.id = str(doc['_id'])
        last_expire_date = course.last_expire_time.split(' ')[0] # 2025-09-25
        if date == last_expire_date: # 说明今天已经消了课时
            continue
        if course.weekday != weekday: # 不是同一天
            continue
        if course.course_left < 1: # 没有课时可以消了
            continue
        
        dt = datetime.strptime(course.course_time.end_time, "%H:%M")
        if now.hour > dt.hour or (now.hour == dt.hour and now.minute >= dt.minute):
            content = {
                'id': course.id,
                'last_expire_time': now_str,
                'course_left': course.course_left-1,
            }
            res, msg = update(doc['_id'], content)
            if res:
                print(f'[{now_str}][{course.content}]: 自动消课时[{course.course_left}][{course.course_left-1}]')
                # 通知前端
                await manager.broadcast(json.dumps(content))
            else:
                print(f'[{now_str}][{course.content}]: 自动消课时失败 [{msg}]')
        


router = APIRouter()
@router.get("/", response_model=List[Course])
async def get_all_course_time():
    cursor = collection.find({'belong_week': 1, 'is_delete': False})
    data = []
    for doc in cursor:
        course = Course(**doc)
        course.id = str(doc['_id'])
        data.append(course)
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
        resp = collection.update_one({"_id":id}, {"$set":to_serializable(updated_course)})
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