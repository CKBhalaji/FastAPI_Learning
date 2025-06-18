from fastapi import  Depends, HTTPException, status, Path, APIRouter
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from ..models import Todos
from ..database import get_db
from typing import Annotated
from .auth import get_current_user

router = APIRouter(
    prefix="/todo",
    tags=["Todos"]
)

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class TodoRequest(BaseModel):
    title : str = Field(min_length=3)
    description : str = Field(min_length=3, max_length=100)
    priority : int = Field(gt=0, lt=6)
    complete : bool
    
@router.get("/", status_code=status.HTTP_200_OK)
def read_all_todo(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed.")
    return db.query(Todos).filter(Todos.owner_id == user.get("id")).all()

@router.get("/{todo_id}", status_code=status.HTTP_200_OK)
def read_todo_by_id(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed.")
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("id")).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Todo not found.")

@router.post("/create_todo", status_code = status.HTTP_201_CREATED)
def create_todo(user: user_dependency, db: db_dependency, todo_request: TodoRequest):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed.")
    todo_model = Todos(**todo_request.model_dump(), owner_id=user.get("id"))
    db.add(todo_model)
    db.commit()
    
@router.put("/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
def update_todo(user: user_dependency, 
                db: db_dependency,
                todo_request: TodoRequest, 
                todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed.")
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("id"))
    todo_post = todo_model.first()
    if todo_post is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Todo not found.")
    # todo_model.title = todo_request.title
    # todo_model.description = todo_request.description
    # todo_model.priority = todo_request.priority
    # todo_model.complete = todo_request.complete
    todo_model.update(todo_request.model_dump(), synchronize_session=False)
    # db.add(todo_model)
    db.commit()
    
@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed.")
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("id")).first()
    if todo_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found.")
    db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("id")).delete()
    db.commit()
