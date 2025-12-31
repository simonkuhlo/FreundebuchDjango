from typing import Annotated, Optional
from fastapi import APIRouter, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from frontend.jinja_templates import templates
from crud import question_collection as question_collection_crud
from crud import question as question_crud
from crud import entry as entry_crud
from schemas.question_collection import QuestionCollectionUpdate, QuestionCollectionRead, QuestionCollectionCreate
from frontend.utils.item_browser import ItemBrowser, ItemBrowserObject, ItemBrowserObjectButton
from data.utils.question_question_collection_relation import modify_questions_of_collection
from . import helpers

router = APIRouter(prefix="/entry_manager", tags=["entry_manager"])

@router.get("/")
async def entry_manager_app(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("apps/admin/entry_manager/main.j2", {"request": request})

@router.get("/browser", response_class=HTMLResponse)
async def render_question_collection_browser(request: Request) -> HTMLResponse:
    browser = helpers.get_entry_browser()
    return browser.render(request)

@router.get("/editor/{entry_id}", response_class=HTMLResponse)
async def collection_editor(request: Request, entry_id: Optional[int] = None, reload_browser: bool = False) -> HTMLResponse:
    entry = None
    if entry_id:
        entry = entry_crud.get(entry_id)
    return templates.TemplateResponse("apps/admin/entry_manager/entry_editor.j2",
                                      {"request": request,
                                       "entry": entry,
                                       "reload_browser": reload_browser
                                       })