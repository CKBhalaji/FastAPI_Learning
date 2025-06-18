from fastapi import  Depends, HTTPException, status, Path, APIRouter
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session
from ..models import Todos, User
from ..database import get_db
from typing import Annotated
from .auth import get_current_user
from passlib.context import CryptContext

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=3)
    
class UserPhoneNumber(BaseModel):
    phonenumber: str
    new_phonenumber : str

class UserResponsemodel(BaseModel):
    email: EmailStr
    username :str
    first_name :str
    last_name :str
    role :str

@router.get("/", status_code=status.HTTP_200_OK)
def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed.")
    user_model = db.query(User).filter(User.id == user.get("id")).first()
    return user_model

@router.put("/changePassword", status_code=status.HTTP_204_NO_CONTENT)
def change_password(user: user_dependency, db: db_dependency, user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed.")
    user_model = db.query(User).filter(User.id == user.get("id")).first()
    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error on the password change.")
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()
    
"""
@router.put("/changephonenumber", status_code=status.HTTP_204_NO_CONTENT)
def change_phone_number(user: user_dependency, db: db_dependency, user_phone_number: UserPhoneNumber):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed.")
    user_model = db.query(User).filter(User.id == user.get("id")).first()
    if not user_model.phone_number == user_phone_number.phonenumber:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Error on changing phone number.")
    user_model.phone_number = user_phone_number.new_phonenumber
    db.add(user_model)
    db.commit()
"""

@router.put("/changephonenumber/{phone_number}", status_code=status.HTTP_204_NO_CONTENT)
def change_phone_number(user: user_dependency, db: db_dependency, phone_number: str):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed.")
    user_model = db.query(User).filter(User.id == user.get("id")).first()
    user_model.phone_number = phone_number
    db.add(user_model)
    db.commit()

    
    