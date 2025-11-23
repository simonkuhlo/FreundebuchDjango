from fastapi import FastAPI
from routes.crud.entries import router as entries_router
from routes.crud.users import router as users_router
from routes.crud.questions import router as questions_router
from routes.crud.question_collections import router as question_collections_router
from routes.crud.answers import router as answers_router
from fastapi.middleware.cors import CORSMiddleware

title: str = "Blume"
summary: str = ""
description: str = ""
version: str = "0.0.1"
origins = [
    "http://localhost:6969",
    "http://77.23.199.184:6969",
    "http://127.0.0.1:6969",
    "http://192.168.178.38:6969",
    "http://meow.technology:6969",
    "http://testing.meow.technology:6969",
]
app = FastAPI(title=title, summary=summary, description=description, version=version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allowed origins
    allow_credentials=True,       # Allow cookies and authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)
app.include_router(entries_router)
app.include_router(users_router)
app.include_router(questions_router)
app.include_router(question_collections_router)
app.include_router(answers_router)
