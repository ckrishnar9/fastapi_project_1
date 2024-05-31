from data import Books
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_books():
    return Books

@app.get("/books/")
async def get_book_by_category(category: str):
    book_by_category = []
    for book in Books:
        if category.casefold() == book.get("category").casefold():
            book_by_category.append(book)
    return book_by_category