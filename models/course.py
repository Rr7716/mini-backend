from typing import List, Optional
from pydantic import BaseModel, field_validator

from models.course_time import CourseTime
from models.student import Student
 
class Course(BaseModel):
    id: Optional[str] = None
    belong_week: Optional[int] = 1 # 属于第几周的
    content: str # 学习内容
    weekday: int # 星期几
    course_time: CourseTime # 所属时间段
    price: int = 100 # 课时费(元/每人)
    per_hour_cost: int = 100 # 课时费(元/每小时)
    students: Optional[List[Student]] = []
    course_left: Optional[int] = 0 # 课时剩余
    grade: Optional[str] = None # 年级
    description: Optional[str] = None
    is_delete: Optional[bool] = False
    last_expire_time: Optional[str] = '2000-01-01 00:00:00' # 上次消课时的时间
    expire_time: Optional[str] = '2000-01-01 00:00:00' # 上上次消课时的时间
    create_time: Optional[str] = '2000-01-01 00:00:00'
    
    # @field_validator('week_day', mode='after')  
    # @classmethod
    # def weekday_is_valid(cls, value: int) -> int:
    #     if value < 1 or value > 7:
    #         raise ValueError(f'{value} is not an even number')
    #     return value  