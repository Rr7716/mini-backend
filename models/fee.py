from typing import Optional
from pydantic import BaseModel
from datetime import datetime 
 
class Fee(BaseModel):
    id: Optional[str] = None
    price: int = 100 # 价格
    hour: int = 60 # 课程分钟数
    description: str = '每小时'
 
