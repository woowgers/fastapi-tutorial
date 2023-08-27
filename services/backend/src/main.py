from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src.database.config import BaseModel, engine
from src.routes import users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:8080", "http://localhost:8080", "https://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)

BaseModel.metadata.create_all(engine)


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")
