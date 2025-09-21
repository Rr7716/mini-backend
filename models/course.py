from typing import List, Optional
from pydantic import BaseModel, field_validator

from models.course_time import CourseTime
from models.student import Student
 
class Course(BaseModel):
    id: Optional[str] = None
    content: str # 学习内容
    weekday: int # 星期几
    course_time_id: str
    course_time: CourseTime # 所属时间段
    price: int = 100 # 课时费(元/每人)
    per_hour_cost: int = 100 # 课时费(元/每小时)
    students: List[Student] = []
    course_left: Optional[int] = 0 # 课时剩余
    grade: Optional[str] = None # 年级
    description: Optional[str] = None
    
    # @field_validator('week_day', mode='after')  
    # @classmethod
    # def weekday_is_valid(cls, value: int) -> int:
    #     if value < 1 or value > 7:
    #         raise ValueError(f'{value} is not an even number')
    #     return value  