from typing import Optional
from apps.Entries.models import EntryV1, CreateCode
from settings import settings

def check_permission(request, entry: Optional[EntryV1] = None) -> bool:
    if entry:
        return can_edit_entry(request, entry)
    return can_create_entry(request)

def can_create_entry(request) -> bool:
    if request.user.is_authenticated:
        if settings.user.max_entries == -1:
            return True
        entries = EntryV1.objects.filter(owner_id=request.user.id)
        if entries.count() >= settings.user.max_entries:
            return False
    else:
        if not request.session.get("code"):
            return False
        if not CreateCode.objects.filter(pk=request.session["code"]).exists():
            return False
    return True

def can_edit_entry(request, entry: EntryV1) -> bool:
    if request.user.is_authenticated:
        if entry.owner == request.user:
            return True
    #TODO Check if session has entry secret stored
    return False