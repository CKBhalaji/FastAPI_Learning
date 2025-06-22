from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, HTTPException, status, Depends, Path, Request
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from ..models import User
from passlib.context import CryptContext
from ..database import get_db
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

SECRET_KEY = "197b2c37c391bed93fe80344fe73b806947a65e36206e05a1a23c2fa12702fe3"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

db_dependency = Annotated[Session, Depends(get_db)]

templates = Jinja2Templates(directory="FastAPI_The_Complete_Course_2025/TodoApp/templates")

### Pages ###

@router.get("/login-page")
def render_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

### Pages ###

@router.get("/register-page")
def render_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

### Endpoints ###

def authenticate_user(username: str, password:str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, role: str, experies_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    experise = datetime.now(timezone.utc) + experies_delta
    encode.update({'exp': experise})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
        return {"username": username, "id": user_id, "user_role": user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")

class CreateUserRequest(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name:str
    password: str 
    role: str
    phone_number : str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
@router.get("/getallusers")
def get_all_users(db: db_dependency):
    return db.query(User).all()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = User(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True,
        phone_number=create_user_request.phone_number
    )
    db.add(create_user_model)
    db.commit()


@router.post("/token", response_model=Token)
def login_for_acces_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
    return {"access_token": token, "token_type": "bearer"}

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(db: db_dependency, user_id: int = Path(gt=0)):
    user_model = db.query(User).filter(User.id == user_id).first()
    if user_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found.")
    db.query(User).filter(User.id == user_id).delete()
    db.commit()