from typing import Optional
from pydantic import BaseModel



class RemoveTimes(BaseModel):
    id: Optional[str] = None
    course_id: str
    create_time: Optional[str] = '2000-01-01 00:00:00'