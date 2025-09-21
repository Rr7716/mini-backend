from typing import List, Optional
from pydantic import BaseModel, field_validator

from models.course_time import CourseTime
from models.fee import Fee 
from models.student import Student
 
class Course(BaseModel):
    id: Optional[str] = None
    students: List[Student] = []
    fee: Fee # 所属价格
    weekday: int # 星期几
    course_time: CourseTime # 所属时间段
    Grade: str # 年级
    Content: str # 学习内容
    description: Optional[str] = None
    
    # @field_validator('week_day', mode='after')  
    # @classmethod
    # def weekday_is_valid(cls, value: int) -> int:
    #     if value < 1 or value > 7:
    #         raise ValueError(f'{value} is not an even number')
    #     return value  