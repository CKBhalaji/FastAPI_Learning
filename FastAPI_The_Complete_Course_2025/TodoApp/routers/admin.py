from fastapi import  Depends, HTTPException, status, Path, APIRouter
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from ..models import Todos
from ..database import get_db
from typing import Annotated
from .auth import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/", status_code=status.HTTP_200_OK)
def red_all(user: user_dependency, db: db_dependency):
    if user is None or user.get("user_role") != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed.")
    return db.query(Todos).all()

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None or user.get("user_role") != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed.")
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not Found.")
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()