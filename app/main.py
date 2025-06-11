from fastapi import FastAPI, status, Response, HTTPException
from fastapi import Depends
from pydantic import BaseModel
import time
import psycopg
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db



models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        # Attempt to connect to the database
        conn = psycopg.connect(host = "localhost",
                               dbname = "fastapi",
                               user = "postgres",
                               password = "2003")
        cursor = conn.cursor()
        print("Database connection successful")
        break  
    except Exception as e:
        print("Database connection failed")
        print(f"Error: {e}")
        time.sleep(2) 
        break  

my_posts = [
    {"title": "Post 1", "content": "Content of Post 1", "published": True, "rating": 5, "post_id": 1},
    {"title": "Post 2", "content": "Content of Post 2", "published": False, "rating": 3, "post_id": 2},
    {"title": "Post 3", "content": "Content of Post 3", "published": True, "rating": None, "post_id": 3}]


def find_post(id):
    for post in my_posts:
        if post['post_id'] == id:
            return post
    return None


def find_index(id):
    for i, post in enumerate(my_posts):
        if post['post_id'] == id:
            return i
    return None


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/posts", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return posts


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post:schemas.postCreate,db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s, %s, %s) RETURNING * """,
    #                (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    # **post.dict()
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

    
    
@app.get("/posts/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (id,))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found"
        )
    return post
    

@app.put("/posts/{id}", response_model=schemas.Post)
def update_post(id: int, post:schemas.postCreate, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
    #                (post.title, post.content, post.published, id))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()
    if updated_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found"
        )
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (id,))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    deleted_post = db.query(models.Post).filter(models.Post.id == id)
    if deleted_post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found"
        )
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



# Users

@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_users(user:schemas.UserCreate, db: Session = Depends(get_db)):
    hassed_password = utils.hash_p(user.password)
    user.password = hassed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user