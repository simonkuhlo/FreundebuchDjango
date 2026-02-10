from ..models import EntryV1
from django.shortcuts import render

def entry_browser(request, page: int = 0, interval: int = 20):
    if page == -1:
        page = len(EntryV1.objects.all()) // interval
    start: int = (page * interval)
    end: int = ((page + 1) * interval)
    entries = EntryV1.objects.all()[start:end]
    last_page: bool = (end > len(entries))
    context = {
        "entries": entries,
        "page": page,
        "interval": interval,
        "last_page": last_page,
    }
    return render(request, "entry_browser/entry_browser.html", context)