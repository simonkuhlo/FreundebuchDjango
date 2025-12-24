import os
from typing import Literal, Annotated
from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from crud import entry as entry_crud, answer as answer_crud
from security.verify_entry_secret import verify_entry_secret
from . import testroutes
from .apps.question_collection_manager.router import router as question_collection_manager_router
from .apps.question_manager.router import router as question_manager_router
from .apps.entry_manager.router import router as entry_manager_router

from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter(tags=["frontend"])
admin_router = APIRouter(prefix="/admin", tags=["admin"])
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory=f"{BASE_DIR}/templates")
admin_router.include_router(question_collection_manager_router)
admin_router.include_router(question_manager_router)
admin_router.include_router(entry_manager_router)
router.include_router(testroutes.router)
router.include_router(admin_router)

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

@router.get("/entry/{entry_id}/editor", response_class=HTMLResponse)
async def show_creator_app(request: Request, entry_id: int):
    entry = entry_crud.get(entry_id)
    return templates.TemplateResponse("apps/entry_editor/entry_editor_app.j2", {"request": request, "entry": entry})

@router.post("/entry/{entry_id}/request_editor", response_class=HTMLResponse)
async def show_creator_app(request: Request, entry_id: int, secret: Annotated[str, Form()]):
    entry = await verify_entry_secret(entry_id, secret)
    return templates.TemplateResponse("apps/entry_editor/entry_editor.j2", {"request": request, "entry": entry})

@router.get("/book", response_class=HTMLResponse)
async def get_book(request: Request):
    return templates.TemplateResponse("book/dynamic_book.j2", {"request": request, "entry_id": 0})

@router.get("/book/entry/{index}/{transition}/", response_class=HTMLResponse)
async def get_entry(request: Request, index: int = 0, transition: Literal["next", "prev"] = "next"):
    match transition:
        case "next":
            index = index + 1
    previous_entry = entry_crud.get(index - 1, False)
    current_entry = entry_crud.get(index, False)
    next_entry = entry_crud.get(index + 1, False)
    return templates.TemplateResponse("book/animated_entry.j2", {"request": request,
                                                        "transition": transition,
                                                        "previous_entry": previous_entry,
                                                        "current_entry": current_entry,
                                                        "next_entry": next_entry
                                                        })

@router.get("/book/answer/{index}/edit/", response_class=HTMLResponse)
async def get_entry(request: Request, answer_id: int = 0):
    answer_object = answer_crud.get(answer_id, False)
    return templates.TemplateResponse("book/elements/answer_edit_input.j2", {"request": request,
                                                        "answer": answer_object,
                                                        })

@router.get("/favicon.ico")
async def get_favicon():
    return FileResponse(f"{BASE_DIR}/static/img/favicon.ico")