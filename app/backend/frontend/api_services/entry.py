from typing import Optional
from backend.schemas.entry import EntryRead
import httpx
import settings

async def get_entry_data(entry_id:int) -> Optional[EntryRead]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.api_url}/crud/entry/{entry_id}")
        try:
            response.raise_for_status()
        except:
            return None
        entry = EntryRead.model_validate(response.json())
        return entry