from fastapi import  Depends, HTTPException, status, Path, APIRouter
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from models import Todos
from database import get_db
from typing import Annotated

router = APIRouter(tags=["Todos"])

db_dependency = Annotated[Session, Depends(get_db)]

class TodoRequest(BaseModel):
    title : str = Field(min_length=3)
    description : str = Field(min_length=3, max_length=100)
    priority : int = Field(gt=0, lt=6)
    complete : bool
    

@router.get("/todo", status_code=status.HTTP_200_OK)
def read_all_todo(db: db_dependency):
    return db.query(Todos).all()

@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
def read_todo_by_id(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Todo not found")

@router.post("/todo/create_todo", status_code = status.HTTP_201_CREATED)
def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()
    
@router.put("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
def update_todo(db: db_dependency,
                todo_request: TodoRequest, 
                todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id)
    todo_post = todo_model.first()
    if todo_post is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Todo not found")
    # todo_model.title = todo_request.title
    # todo_model.description = todo_request.description
    # todo_model.priority = todo_request.priority
    # todo_model.complete = todo_request.complete
    todo_model.update(todo_request.model_dump(), synchronize_session=False)
    # db.add(todo_model)
    db.commit()
    
@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
