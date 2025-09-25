import datetime
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from routers.router_fee import router as fee
from routers.router_course import autp_expire, router as course, router_ws
from routers.router_course_time import router as course_time
from routers.router_student import router as student
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from contextlib import asynccontextmanager

scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时
    scheduler.add_job(autp_expire, "interval", seconds=10)
    scheduler.start()
    print("Scheduler 已启动")
    
    yield   # <-- 应用运行中
    
    # 关闭时
    scheduler.shutdown()
    print("Scheduler 已关闭")

app = FastAPI(lifespan=lifespan)
app.include_router(router_ws)
app.include_router(fee, prefix="/fee", tags=['课时费'])
app.include_router(course, prefix="/course", tags=['课程'])
app.include_router(course_time, prefix="/course_time", tags=['课程时间'])
app.include_router(student, prefix="/student", tags=['学生'])

@app.get('/index')
def root():
    return {'name': '123'}