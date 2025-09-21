from fastapi import FastAPI, HTTPException
from routers.router_fee import router as fee
from routers.router_course import router as course
from routers.router_course_time import router as course_time
from routers.router_student import router as student

app = FastAPI()
app.include_router(fee, prefix="/fee", tags=['课时费'])
app.include_router(course, prefix="/course", tags=['课程'])
app.include_router(course_time, prefix="/course_time", tags=['课程时间'])
app.include_router(student, prefix="/student", tags=['学生'])

@app.get('/index')
def root():
    return {'name': '123'}
