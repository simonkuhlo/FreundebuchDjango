import os
from typing import Literal, Annotated
from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from crud import entry, answer
from . import testroutes

from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter(tags=["frontend"])
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory=f"{BASE_DIR}/templates")

router.include_router(testroutes.router)

# show_... : returns fully rendered page including base template
# get_...  : returns a single element

@router.get("/", response_class=HTMLResponse)
async def show_index(request: Request):
    return templates.TemplateResponse("index.j2", {"request": request})

@router.get("/dedication", response_class=HTMLResponse)
async def show_dedication_page(request: Request):
    return templates.TemplateResponse("dedication.j2", {"request": request})

@router.get("/viewer", response_class=HTMLResponse)
async def show_viewer_app(request: Request):
    return templates.TemplateResponse("viewer.j2", {"request": request})

@router.get("/creator", response_class=HTMLResponse)
async def show_creator_app(request: Request):
    return templates.TemplateResponse("creator.j2", {"request": request})

@router.get("/canvas", response_class=HTMLResponse)
async def show_creator_app(request: Request):
    return templates.TemplateResponse("canvas.j2", {"request": request})

@router.get("/entry/creator", response_class=HTMLResponse)
async def show_creator_app(request: Request):
    return templates.TemplateResponse("apps/entry_creator_app.j2", {"request": request})

@router.post("/entry/creator", response_class=HTMLResponse)
async def create_entry_endpoint(user_id: Annotated[int, Form()]):
    await create_entry.create_entry(user_id)

@router.get("/book", response_class=HTMLResponse)
async def get_book(request: Request):
    return templates.TemplateResponse("book/dynamic_book.j2", {"request": request, "entry_id": 0})

@router.get("/book/entry/{index}/{transition}/", response_class=HTMLResponse)
async def get_entry(request: Request, index: int = 0, transition: Literal["next", "prev"] = "next"):
    match transition:
        case "next":
            index = index + 1
    previous_entry = entry.get(index - 1, False)
    current_entry = entry.get(index, False)
    next_entry = entry.get(index + 1, False)
    return templates.TemplateResponse("book/animated_entry.j2", {"request": request,
                                                        "transition": transition,
                                                        "previous_entry": previous_entry,
                                                        "current_entry": current_entry,
                                                        "next_entry": next_entry
                                                        })

@router.get("/book/answer/{index}/edit/", response_class=HTMLResponse)
async def get_entry(request: Request, answer_id: int = 0):
    answer_object = answer.get(answer_id, False)
    return templates.TemplateResponse("book/elements/answer_edit_input.j2", {"request": request,
                                                        "answer": answer_object,
                                                        })

@router.get("/favicon.ico")
async def get_favicon():
    return FileResponse(f"{BASE_DIR}/static/img/favicon.ico")