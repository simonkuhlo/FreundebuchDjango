from typing import Optional
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from Entries.models import EntryV1, CreateCode
from Entries.custom_fields import shortcuts

def edit(request, entry_id: int):
    entry = EntryV1.objects.filter(id=entry_id).first()
    if not entry:
        return render(request, "main/status_pages/not_found.html", {"message": "Entry not found..."})
    if request.user != entry.owner:
        return render(request, "main/status_pages/permission_denied.html")
    match request.method:
        case 'POST':
            return
        case 'GET':
            entry.rendered_custom_field = shortcuts.render_field_str(entry.custom_field_mode, entry)
            context = {
                'entry': entry,
            }
            return render(request, "creator/creator.html", context=context)
        case _:
            return HttpResponseNotAllowed(['GET', 'POST'])

def delete(request, entry_id: int):
    entry = EntryV1.objects.filter(id=entry_id).first()
    if not entry:
        return render(request, "main/status_pages/not_found.html", {"message": "Entry not found..."})
    if request.user != entry.owner:
        return render(request, "main/status_pages/permission_denied.html")
    match request.method:
        case 'POST':
            confirm_id = request.POST.get('confirm_id')
            if entry_id != int(confirm_id):
                return render(request, "editor/delete_entry.html", {"error": "Confirmation failed..."})
            entry.delete()
            return render(request, "editor/delete_success.html")
        case 'GET':
            return render(request, "editor/delete_entry.html")
        case _:
            return HttpResponseNotAllowed(['GET', 'POST'])



