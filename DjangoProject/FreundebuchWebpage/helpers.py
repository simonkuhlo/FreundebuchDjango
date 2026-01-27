from Entries.models import EntryV1, CreateCode
from settings import settings


def can_create_entry(request) -> bool:
    if request.user.is_authenticated:
        entries = EntryV1.objects.filter(owner_id=request.user.id)
        if entries.count() >= settings.user.max_entries:
            return False
    else:
        if not request.session.get("code"):
            return False
        if not CreateCode.objects.filter(pk=request.session["code"]).exists():
            return False
    return True