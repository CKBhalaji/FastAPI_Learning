from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from models import User
from passlib.context import CryptContext
from database import get_db
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["User"])

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

db_dependency = Annotated[Session, Depends(get_db)]

def authenticate_user(username: str, password:str, db):
    user = db.query(User).filter(User.email == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return True

class CreateUserRequest(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name:str
    password: str 
    role: str

@router.post("/auth", status_code=status.HTTP_201_CREATED)
def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = User(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )
    db.add(create_user_model)
    db.commit()


@router.post("/token")
def login_for_acces_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return "Failed Authentication"
    return "Sucessfull Authentication"