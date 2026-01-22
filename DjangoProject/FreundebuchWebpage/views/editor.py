from typing import Optional
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Entries.models import EntryV1, CreateCode
from Entries.custom_fields import shortcuts

def edit(request, entry_id: int):
    entry = EntryV1.objects.get(id=entry_id)
    match request.method:
        case 'POST':
            return
        case 'GET':
            context = {
                'entry': entry,
            }
            return render(request, "creator/creator.html", context=context)
        case _:
            return HttpResponse(status=404)