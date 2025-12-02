from fastapi import APIRouter
from schemas.entry import EntryCreate, EntryUpdate, EntryRead

router = APIRouter(prefix="/entry", tags=["entry_service"])

@router.post("/create", response_model=EntryRead)
async def create_entry(entry: EntryCreate) -> EntryRead:

    return