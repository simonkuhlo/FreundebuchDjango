from typing import Annotated

from schemas.entry import EntryCreate
from .crud_handler_router import CRUDHandlerRouter
from fastapi import APIRouter, Request, Form, HTTPException
from crud import entry


router = CRUDHandlerRouter(entry)

@router.post("/form_create")
async def create_otp(request: Request, new_entry: Annotated[EntryCreate, Form()]):
    created_entry = entry.create(new_entry)
    return created_entry