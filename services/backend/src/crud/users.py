from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas.token import Status
from src.schemas.users import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def read_all(db: Session) -> list[User]:
    return db.query(User).all()


def read(id: int, db: Session) -> User:
    try:
        user = db.query(User).where(User.id == id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found.")
    return user


def create(schema: UserCreate, db: Session) -> User:
    schema.password = pwd_context.encrypt(schema.password)
    try:
        user = User(**schema.model_dump())
        db.add(user)
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=401, detail="Failed to create user.")
    return user


def delete(id: int, current_user: User, db: Session) -> Status:
    user = read(id, db)
    if user.id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this user.")

    deleted_count = db.query(User).filter(User.id == id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="User not found.")

    db.commit()
    return Status(message="User has been deleted.")


def make_friends(id1: int, id2: int, db: Session) -> list[User]:
    user1 = read(id1, db)
    user2 = read(id2, db)
    user1.friends.append(user2)
    user2.friends.append(user1)
    db.commit()
    return user1.friends
