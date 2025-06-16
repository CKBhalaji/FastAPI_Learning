from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

from FastAPI_The_Complete_Course_2025.Project_1_FastAPI_Books import books

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating : int
    published_date: int
    
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(default=None, description="ID of the book, will be auto-generated if not provided")
    title: str = Field(min_length=3, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=500)
    rating: int = Field(gt=0, lt=6, description="Rating must be between 1 and 5")
    published_date: int = Field(gt=1999, lt=2025, description="Published date must be between 1 and 2025")
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "description": "A novel set in the Roaring Twenties, exploring themes of decadence and excess.",
                "rating": 4,
                "published_date": 2000
            }
        }
    }
    
class bookResponse(BaseModel):
    id: int
    title: str
    

BOOKS = [
    Book(1, "1984", "George Orwell", "Dystopian novel set in totalitarian society", 5, 2020),
    Book(2, "To Kill a Mockingbird", "Harper Lee", "Novel about racial injustice in the Deep South", 4, 2020),
    Book(3, "The Great Gatsby", "F. Scott Fitzgerald", "Story of the Jazz Age in the United States", 4, 2019),
    Book(4, "Pride and Prejudice", "Jane Austen", "Romantic novel about manners and marriage", 2, 2018),
    Book(5, "The Catcher in the Rye", "J.D. Salinger", "Novel about teenage angst and alienation", 3, 2017),
    Book(6, "Hidden Figures", "Margot Lee Shetterly","Story of African-American", 5, 2016),
    Book(7, "The Alchemist", "Paulo Coelho", "Philosophical novel about following one's dreams", 1, 2015)
]

@app.get("/books", status_code=status.HTTP_200_OK)
def read_all_books():
    return BOOKS

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
def read_book(book_id: int = Path(gt = 0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/", status_code=status.HTTP_200_OK)
def read_book_by_rating(book_rating: int = Query(gt = 0, lt = 6)):
    books_reatun = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_reatun.append(book)
    return books_reatun

@app.get("/books/published_date/", status_code=status.HTTP_200_OK)
def filter_by_published_date(filter_by_published_date: int = Query(gt = 1999, lt = 2025)):
    books_published_date = []
    for book in BOOKS:
        if book.published_date == filter_by_published_date:
            books_published_date.append(book)
    return books_published_date

@app.post("/books/create_book", status_code=status.HTTP_201_CREATED) 
def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    # print(type(new_book))
    return {"message": "Book added successfully", "book": new_book}


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
        
@app.put("/book/update_book", status_code=status.HTTP_204_NO_CONTENT)
def update_book(book: BookRequest):
    book_to_update = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_to_update = True
            break
    if not book_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int = Path(gt = 0)):
    book_to_delete = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            del BOOKS[i]
            book_to_delete = True
            break
    if not book_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")






