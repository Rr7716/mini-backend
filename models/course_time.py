from typing import Optional
from pydantic import BaseModel
 
class CourseTime(BaseModel):
    id: Optional[str] = None
    start_time: str
    end_time:str
 
