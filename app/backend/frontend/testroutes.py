import os
from typing import Annotated
from fastapi import APIRouter, HTTPException, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from crud import entry as entry_crud, question as question_crud
from schemas.entry import EntryCreate

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory=f"{BASE_DIR}/templates")
router = APIRouter(prefix="/tests")

@router.get("/admin/entry_manager", response_class=HTMLResponse)
async def admin_entry_manager(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("apps/admin/entry_manager/main.j2", {"request": request})

@router.get("/admin/entry_browser", response_class=HTMLResponse)
async def admin_entry_browser(request: Request) -> HTMLResponse:
    entries = entry_crud.list()
    return templates.TemplateResponse("apps/admin/entry_manager/entry_browser.j2", {"request": request, "entries": entries})

@router.get("/admin/entry_details/{entry_id}", response_class=HTMLResponse)
async def admin_entry_details(request: Request, entry_id: int) -> HTMLResponse:
    entry = entry_crud.get_admin(entry_id)
    return templates.TemplateResponse("apps/admin/entry_manager/entry_details.j2", {"request": request, "entry": entry})

@router.get("/admin/question_manager", response_class=HTMLResponse)
async def admin_question_manager(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("apps/admin/question_manager/question_manager_app.j2", {"request": request})

@router.get("/admin/question_browser", response_class=HTMLResponse)
async def admin_question_browser(request: Request) -> HTMLResponse:
    questions = question_crud.list()
    return templates.TemplateResponse("apps/admin/question_manager/question_browser.j2", {"request": request, "questions": questions})

@router.get("/admin/question_editor/{question_id}", response_class=HTMLResponse)
async def admin_question_editor(request: Request, question_id: int) -> HTMLResponse:
    question = question_crud.get(question_id)
    return templates.TemplateResponse("apps/admin/question_manager/question_editor.j2", {"request": request, "question": question})