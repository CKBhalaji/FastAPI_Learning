from hmac import new
from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title":"Title One", "auther":"Author One", "category": "Science"},
    {"title":"Title Two", "auther":"Author Two", "category": "Science"},
    {"title":"Title Three", "auther":"Author Three", "category": "History"},
    {"title":"Title Four", "auther":"Author Four", "category": "Math"},
    {"title":"Title Five", "auther":"Author Five", "category": "Math"},
    {"title":"Title Six", "auther":"Author Two", "category": "Math"}
]

@app.get("/books")
def read_all_books():
    return BOOKS

@app.get("/books/author")
def read_books_by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("auther").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_title}")
def read_book_by_title(book_title: str):
    for book in BOOKS:
        if book["title"].lower() == book_title.lower():
            return book
    return {"message": "Book not found"}

@app.get("/books/")
def read_books_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
def read_author_category_by_query(book_author: str, category: str = None):
    books_to_return = []
    for book in BOOKS:
        if book.get("auther").casefold() == book_author.casefold() and book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
def create_book(new_book = Body()):
    BOOKS.append(new_book)
    return {"message": "Book added successfully", "book": new_book}

@app.put("/books/update_book")
def update_book(updated_book = Body()):
    for i in range(len(BOOKS)): 
        if BOOKS[i].get("title").lower() == updated_book.get("title").lower():
            BOOKS[i] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}
    return {"message": "Book not found"}

@app.patch("/books/patch_book")
def patch_book(book_title: str, book_update = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").lower() == book_title.lower():
            BOOKS[i].update(book_update)
            return {"message": "Book patched successfully", "book": BOOKS[i]}
    return {"message": "Book not found"}

@app.delete("/books/delete_book/{book_title}")
def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").lower() == book_title.lower():
            del BOOKS[i]
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}

