from fastapi import FastAPI, Form, Header, HTTPException, Request, status
from fastapi.responses import JSONResponse
from faker import Faker
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid1

app = FastAPI()
faker = Faker()


class NegativeNumberException(Exception):
    def __init__(self, books_to_return: int):
        self.books_to_return = books_to_return


class InvalidUserException(Exception):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book",
                                       min_length=1,
                                       max_length=255)
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": {
                "id": str(uuid1()),
                "title": "A Song of Ice and Fire",
                "author": "George R.R Martin",
                "description": "The world of Westeros is thrown into chaos when the king dies and the lineage is rumored to be tainted.",
                "rating": 95,
            }
        }


class BookNoRating(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book",
                                       min_length=1,
                                       max_length=255)


BOOKS = []


@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request: Request,
                                            exception: NegativeNumberException):
    return JSONResponse(
        status_code=418,
        content={"message": f"{exception.books_to_return}? Read something!!!"}
    )


@app.exception_handler(InvalidUserException)
async def invalid_user_exception_handler(request: Request,
                                         exception: InvalidUserException):
    return JSONResponse(
        status_code=401,
        content={'message': "Your credentials were invalid. Please try again."}
    )


@app.get("/header")
async def read_header(random_header: Optional[str] = Header(None)):
    return {"Random-Header": random_header}


@app.post("/login_with_header/{book_id}", status_code=status.HTTP_202_ACCEPTED)
async def login(book_num: int, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    if username != "FastAPIUser" or password != "test1234":
        raise InvalidUserException(username=username, password=password)
    else:
        if book_num > len(BOOKS) or book_num < 0:
            return "Book does not exist."
        return BOOKS[book_num]


@app.post("/login_without_header/{book_id}", status_code=status.HTTP_202_ACCEPTED)
async def login(book_id: UUID, username: Optional[str] = Form(), password: Optional[str] = Form()):
    if username != "FastAPIUser" or password != "test1234":
        raise InvalidUserException(username=username, password=password)
    else:
        for x in BOOKS:
            if x.id == book_id:
                return x
        raise exception_404()


@app.get("/")
async def read_all_books(books_to_return: Optional[int] = None):
    if books_to_return and books_to_return < 0:
        raise NegativeNumberException(books_to_return=books_to_return)
    if len(BOOKS) < 1:
        create_books_no_api()
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        return BOOKS[:books_to_return]
    return BOOKS


@app.get("/book/{book_id}")
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x
    raise exception_404()


@app.get("/book/rating/{book_id}", response_model=BookNoRating)
async def read_book_no_rating(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x
    raise exception_404()


@app.put("/{book_id}")
async def update_book(book_id: UUID, book: Book):
    for x in range(len(BOOKS)):
        if BOOKS[x].id == book_id:
            BOOKS[x] = book
            return BOOKS[x]
    raise exception_404()


@app.delete("/{book_id}")
async def delete_book(book_id: UUID, book: Book):
    for x in range(len(BOOKS)):
        if BOOKS[x].id == book_id:
            del BOOKS[x]
            return f"{book_id} has been deleted."
    raise exception_404()


@app.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    BOOKS.append(book)
    return book


def create_books_no_api():
    for i in range(5):
        i = Book(
            id=str(uuid1()),
            title=" ".join(faker.words(6)).title(),
            author=faker.name(),
            description=faker.paragraph(nb_sentences=4, variable_nb_sentences=False),
            rating=faker.random_int(0, 100),
        )
        BOOKS.append(i)


def exception_404():
    return HTTPException(status_code=404,
                         detail="Book not found.",
                         headers={"X-Header_Error": "Nothing to be seen at the UUID."})
