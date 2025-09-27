from typing import Optional
from pydantic import BaseModel
from datetime import datetime 
 
class Student(BaseModel):
    id: Optional[str] = None
    en_name: str
    cn_name: Optional[str] = ''
    age: Optional[int] = 5
    gender: Optional[str] = 'boy'
    grade: Optional[str] = '幼儿园'