from typing import Literal

import settings
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from services.get_entry_data import get_entry_data

app = FastAPI(title=settings.app_title, summary=settings.app_summary, description=settings.app_description, version=settings.app_version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.app_origins,        # Allowed origins
    allow_credentials=True,       # Allow cookies and authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)

# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory="templates")
templates.env.globals["api_url"] = settings.api_url

# show_... : returns fully rendered page including base template
# get_...  : returns a single element

@app.get("/", response_class=HTMLResponse)
async def show_index(request: Request):
    return templates.TemplateResponse("index.j2", {"request": request})

@app.get("/test", response_class=HTMLResponse)
async def get_partial(request: Request):
    return templates.TemplateResponse("partial.j2", {"request": request})

@app.get("/dedication", response_class=HTMLResponse)
async def show_dedication_page(request: Request):
    return templates.TemplateResponse("dedication.j2", {"request": request})

@app.get("/viewer", response_class=HTMLResponse)
async def show_viewer_app(request: Request):
    return templates.TemplateResponse("viewer.j2", {"request": request})

@app.get("/creator", response_class=HTMLResponse)
async def show_creator_app(request: Request):
    return templates.TemplateResponse("creator.j2", {"request": request})

@app.get("/canvas", response_class=HTMLResponse)
async def show_creator_app(request: Request):
    return templates.TemplateResponse("canvas.j2", {"request": request})

@app.get("/book", response_class=HTMLResponse)
async def get_book(request: Request):
    return templates.TemplateResponse("book/dynamic_book.j2", {"request": request, "entry_id": 0})

@app.get("/book/next_page/{index}", response_class=HTMLResponse)
async def get_next_page(request: Request, index: int = 0):
    return templates.TemplateResponse("book/book_page.j2", {"request": request, "page_index": index})

@app.get("/book/entry/{index}/{transition}/", response_class=HTMLResponse)
async def get_entry(request: Request, index: int = 0, transition: Literal["next", "prev"] = "next"):
    match transition:
        case "next":
            index = index + 1
    previous_entry = await get_entry_data(index - 1)
    current_entry = await get_entry_data(index)
    next_entry = await get_entry_data(index + 1)
    return templates.TemplateResponse("book/animated_entry.j2", {"request": request,
                                                        "transition": transition,
                                                        "previous_entry": previous_entry,
                                                        "current_entry": current_entry,
                                                        "next_entry": next_entry
                                                        })

@app.get("/favicon.ico")
async def get_favicon():
    return FileResponse("static/img/favicon.ico")