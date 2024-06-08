from typing import Optional
from data import Books
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    author: str
    book_title: str
    category: str
    year: int

    def __init__(self, id, author, book_title, category, year):
        self.id = id
        self.author = author
        self.book_title = book_title
        self.category = category
        self.year = year


class Book_Request(BaseModel):
    id: Optional[int] = Field(title="ID not required")
    author: str = Field(min_length=3)
    book_title: str = Field(min_length=3)
    category: str = Field(min_length=3)
    year: int = Field(gt=1900, lt=2024)


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


@app.get("/books/")
async def get_book_by_year(year: int):
    book_by_year = []
    for book in Books:
        if year == book.get(year):
            book_by_year.append(book)
    return book_by_year
 