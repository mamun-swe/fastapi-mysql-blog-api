from pydantic import BaseModel
from datetime import datetime

class BlogBase(BaseModel):
    title: str
    description: str
    created_at: datetime

class BlogCreate(BaseModel):
    title: str
    description: str