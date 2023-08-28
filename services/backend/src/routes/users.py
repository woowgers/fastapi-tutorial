from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import src.crud.users as crud
from src.auth.jwthandler import (ACCESS_TOKEN_EXPIRE_MINUTES,
                                 create_access_token, get_current_user)
from src.auth.users import validate_user
from src.database.config import get_db
from src.database.models import User
from src.schemas.token import Status
from src.schemas.users import User as UserSchema
from src.schemas.users import UserCreate

router = APIRouter()


@router.post("/register", response_model=UserSchema)
def create(user: UserCreate, db: Session = Depends(get_db)) -> User:
    return crud.create(user, db)


@router.post("/login")
def login(user_form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = validate_user(db, user_form)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    token = jsonable_encoder(access_token)
    content = {"message": "You have successfully logged in."}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="lax",
        secure=False,
    )
    return response


@router.get("/users", response_model=list[UserSchema])
def read_all_users(db: Session = Depends(get_db)):
    return crud.read_all(db)


@router.get("/users/me", response_model=UserSchema)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.read(user_id, db)


@router.delete("/users/{user_id}", response_model=Status)
def delete_user(id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return crud.delete(id, current_user, db)


@router.post("/users/{user_id}/make_friend", response_model=list[UserSchema])
def make_friend(user_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return crud.make_friends(current_user.id, user_id, db)
