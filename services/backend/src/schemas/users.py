from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    full_name: str
    password: str

    class Config:
        from_attributes = True


class UserShort(BaseModel):
    id: int
    username: str


class UserCreate(BaseModel):
    username: str
    full_name: str
    password: str


class UserUpdate(BaseModel):
    username: str | None
    full_name: str | None
    password: str | None
