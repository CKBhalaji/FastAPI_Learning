from calendar import c
from datetime import datetime
from typing import Annotated, Optional
from httpx import post
from pydantic import BaseModel, EmailStr, conint

class Config:
    from_attributes = True
    
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class postCreate(PostBase):
    pass

class Post(PostBase):
    id: int 
    created_at: datetime
    owner_id: int
    owner: UserOut
    
class PostOut(BaseModel):
    Post: Post
    votes: int
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    
class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, conint(ge=0, le=1)]
