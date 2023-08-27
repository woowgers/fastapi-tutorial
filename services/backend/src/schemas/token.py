from pydantic import BaseModel


class Token(BaseModel):
    username: str | None


class Status(BaseModel):
    message: str
