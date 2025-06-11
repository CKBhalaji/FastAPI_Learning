from datetime import datetime
from venv import create
from pydantic import BaseModel, EmailStr

    
class postBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class postCreate(postBase):
    pass

class Post(postBase):
    id: int 
    created_at: datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
