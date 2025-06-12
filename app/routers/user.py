from fastapi import FastAPI, status, Response, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_users(user:schemas.UserCreate, db: Session = Depends(get_db)):
    hassed_password = utils.hash_p(user.password)
    user.password = hassed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} was not found"
        )
    return user
