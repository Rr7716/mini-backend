from typing import Optional
from pydantic import BaseModel
from datetime import datetime 
 
class Student(BaseModel):
    id: Optional[str] = None
    cn_name: str
    en_name: str
    age: int