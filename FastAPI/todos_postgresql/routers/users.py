from database import engine, SessionLocal
from fastapi import APIRouter, Depends, HTTPException
import models
from pydantic import BaseModel
from routers.auth import get_password_hash, get_current_user, get_user_exception, token_exception, verify_password
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


@router.get("/")
async def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()


@router.get("/{user_id}")
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.id == user_id).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_model


@router.get("/user")
async def get_user_by_query(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.id == user_id).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_model


@router.put("/user/password")
async def user_password_change(user_verfication: UserVerification,
                               user: dict = Depends(get_current_user),
                               db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()

    user_model = db.query(models.Users).filter(models.Users.id == user.get("user_id")).first()

    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")

    if user_verfication.username == user_model.username \
            and verify_password(user_verfication.password, user_model.hashed_password):

        user_model.hashed_password = get_password_hash(user_verfication.new_password)
        db.add(user_model)
        db.commit()

        return {
            "status": 201,
            "transaction": "Successful"
        }
    return token_exception()


@router.delete("/user")
async def delete_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):

    if user is None:
        raise get_user_exception()

    user_model = db.query(models.Users).filter(models.Users.id == user.get("user_id")).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.query(models.Users).filter(models.Users.id == user.get("user_id")).delete()
    db.commit()

    return {
        "status": 200,
        "transaction": f"{user.get('user_id')} has been deleted."
    }
