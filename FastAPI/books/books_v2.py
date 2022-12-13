from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

BOOKS = {
    "book_1": {
        "title": "Title One",
        "author": "Author One",
    },
    "book_2": {
        "title": "Title Two",
        "author": "Author Two",
    },
    "book_3": {
        "title": "Title Three",
        "author": "Author Three",
    },
    "book_4": {
        "title": "Title Four",
        "author": "Author Four",
    },
    "book_5": {
        "title": "Title Five",
        "author": "Author Five",
    },
}


# print(list(BOOKS.keys())[-1])


@app.get("/")
async def read_all_books():
    return BOOKS


@app.get("/skip")
async def get_books_except(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]


@app.get("/read_book/")
async def new_read_book(book_name: str):
    return BOOKS[book_name]


@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 0

    if len(BOOKS) > 0:
        x = int(list(BOOKS.keys())[-1].split("_")[-1])
        current_book_id = x + 1 if x > current_book_id else current_book_id

    BOOKS[f"books_{current_book_id}"] = {
        "title": book_title,
        "author": book_author,
    }

    return BOOKS[f"books_{current_book_id}"]


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_info = {"title": book_title, "author": book_author}
    BOOKS[book_name] = book_info

    return BOOKS[book_name]


@app.delete("/{book_name}")
async def delete_book(book_name: str):
    del BOOKS[book_name]
    return f"Book {book_name} has been deleted."


@app.delete("/delete_book/")
async def new_delete_book(book_name: str):
    del BOOKS[book_name]
    return f"Book {book_name} has been deleted."


class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Up"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "Down"}
    if direction_name == DirectionName.east:
        return {"Direction": direction_name, "sub": "Right"}
    return {"Direction": direction_name, "sub": "Left"}
