from fastapi import status
from ..routers.todos import get_current_user
from ..database import get_db
from ..main import app
from ..models import Todos
from .utils import override_get_db, override_get_current_user, client, TestingSessionLocal, test_todo

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_read_all_authenticated(test_todo):
    response = client.get("/todos")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{"complete": False, 
                                "title": "Learn Fast API",
                                "description": "Learnig is fun", 
                                "id": 1, 
                                "priority": 5, 
                                "owner_id": 1}]
    
def test_read_one_authenticated(test_todo):
    response = client.get("/todos/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"complete": False, 
                                "title": "Learn Fast API",
                                "description": "Learnig is fun", 
                                "id": 1, 
                                "priority": 5, 
                                "owner_id": 1}
    
def test_read_one_authentication_not_found():
    response = client.get("/todos/todo/2020")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found."}
    
def test_create_todo(test_todo):
    request_data={
        "title": "hi!",
        "description": "thie is",
        "priority": 5,
        "complete": False,
    }
    response = client.post("/todos/todo/create_todo", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 2).first()
    assert model.title == request_data.get('title')
    assert model.description == request_data.get('description')
    assert model.priority == request_data.get('priority')
    assert model.complete == request_data.get('complete')

def test_update_todo(test_todo):
    request_data={
        'title':"change the title",
        'description':"Be consistent",
        'priority': 5,
        'complete': False,
    }
    response = client.put("/todos/todo/1", json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model.title == request_data.get('title')
    assert model.description == request_data.get('description')
    assert model.priority == request_data.get('priority')
    assert model.complete == request_data.get('complete')
    
def test_update_todo_not_found(test_todo):
    request_data={
        'title':"change the title",
        'description':"Be consistent",
        'priority': 5,
        'complete': False,
    }
    response = client.put("/todos/todo/2020", json=request_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found."}
    
def test_delete_todo(test_todo):
    response = client.delete("/todos/todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None
    
def test_delete_todo_not_found(test_todo):
    response = client.delete("/todos/todo/2020")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found."}
    

