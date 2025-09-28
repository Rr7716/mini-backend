from typing import Optional
from pydantic import BaseModel

from models.course_time import CourseTime


class TakeLeave(BaseModel):
    id: Optional[str] = None
    course_id: str
    reason: Optional[str] = None
    create_time: Optional[str] = '2000-01-01 00:00:00'