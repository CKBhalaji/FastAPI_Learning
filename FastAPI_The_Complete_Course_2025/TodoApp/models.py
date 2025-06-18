from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, server_default="True", nullable=False)
    role = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)

class Todos(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    complete = Column(Boolean, server_default="False", nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete= "CASCADE"), nullable=False)