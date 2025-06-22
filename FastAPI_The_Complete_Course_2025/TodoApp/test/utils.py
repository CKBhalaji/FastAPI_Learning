import email
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from ..database import Base
from ..main import app
import pytest
from ..models import Todos, User
from ..routers.auth import bcrypt_context

SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def override_get_current_user():
    return {'username': 'qwertytest', 'id': 1, 'user_role': 'admin'}

client = TestClient(app)
  
@pytest.fixture
def test_todo():
    todo = Todos(
        title="Learn Fast API",
        description="Learnig is fun",
        priority=5,
        complete=False,
        owner_id=1,
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()
        
@pytest.fixture
def test_user():
    user = User(
        username="qwertytest",
        email="qwertytest@gmail.com",
        first_name="qwertytest",
        last_name="uiopastest",
        hashed_password=bcrypt_context.hash("qwertytest"),
        role="admin",
        phone_number="9789559266",   
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM Users;"))
        connection.commit()