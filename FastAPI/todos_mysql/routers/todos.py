import sys

sys.path.append("..")

from database import engine, SessionLocal
from fastapi import APIRouter, Depends, HTTPException
import models
from pydantic import BaseModel, Field
from .auth import get_current_user, get_user_exception
from sqlalchemy.orm import Session
from typing import Optional

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="The priority must be between 1-5.")
    complete: bool

    class Config:
        schema_extra = {
            "example": {
                "title": "Go to Costco",
                "description": "Get rice for the week.",
                "priority": 4,
                "complete": False,
            }
        }


@router.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@router.get("/user")
async def read_all_by_user(user: dict = Depends(get_current_user),
                           db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    return db.query(models.Todos) \
        .filter(models.Todos.user_id == user.get("user_id")).all()


@router.get("/{todo_id}")
async def read_todo(todo_id: int,
                    user: dict = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    todo_model = db.query(models.Todos) \
        .filter(models.Todos.id == todo_id) \
        .filter(models.Todos.user_id == user.get("user_id")) \
        .first()
    if todo_model is None:
        raise http_exceptions(404)
    return todo_model


@router.post("/")
async def create_todo(todo: Todo,
                      user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    todo_model.user_id = user.get("user_id")

    db.add(todo_model)
    db.commit()

    return successful_response(201)


@router.put("/{todo_id}")
async def update_todo(todo_id: int, todo: Todo,
                      user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()

    todo_model = db.query(models.Todos) \
        .filter(models.Todos.id == todo_id) \
        .filter(models.Todos.user_id == user.get("user_id")) \
        .first()
    if todo_model is None:
        raise http_exceptions(404)

    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return successful_response(200)


@router.delete("/{todo_id}")
async def delete_todo(todo_id: int,
                      user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()

    todo_model = db.query(models.Todos) \
        .filter(models.Todos.id == todo_id) \
        .filter(models.Todos.user_id == user.get("user_id")) \
        .first()
    if todo_model is None:
        raise http_exceptions(404)

    db.query(models.Todos).filter(models.Todos.id == todo_id).delete()
    db.commit()

    return successful_response(201)


def successful_response(status_code: int):
    return {
        "status": status_code,
        "transaction": "Successful"
    }


def http_exceptions(status_code):
    match status_code:
        case 403:
            return HTTPException(status_code=403, detail="Invalid credentials.")
        case 404:
            return HTTPException(status_code=404, detail="Todo not found.")
