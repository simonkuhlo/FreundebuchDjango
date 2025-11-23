import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

title: str = "BlumeFrontend"
summary: str = ""
description: str = ""
version: str = "0.0.1"
origins = [
    "http://localhost:8081",
    "http://localhost:6969",
]
api_url = "http://localhost:8081/"

app = FastAPI(title=title, summary=summary, description=description, version=version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allowed origins
    allow_credentials=True,       # Allow cookies and authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)

# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory="templates")
templates.env.globals["api_url"] = api_url

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.j2", {"request": request})

@app.get("/test", response_class=HTMLResponse)
async def partial(request: Request):
    return templates.TemplateResponse("partial.j2", {"request": request})

@app.get("/dedication", response_class=HTMLResponse)
async def partial(request: Request):
    return templates.TemplateResponse("dedication.j2", {"request": request})

@app.get("/viewer", response_class=HTMLResponse)
async def viewer(request: Request):
    return templates.TemplateResponse("viewer.j2", {"request": request})

@app.get("/creator", response_class=HTMLResponse)
async def viewer(request: Request):
    return templates.TemplateResponse("creator.j2", {"request": request})

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/img/favicon.ico")