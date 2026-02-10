from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from Entries.models import EntryV1


def delete(request, entry_id: int):
    entry = EntryV1.objects.filter(id=entry_id).first()
    context = {"entry": entry}
    if not entry:
        return render(request, "main/status_pages/not_found.html", {"message": "Entry not found..."})
    if request.user != entry.owner:
        return render(request, "main/status_pages/permission_denied.html")
    match request.method:
        case 'POST':
            confirm_id = request.POST.get('confirm_id')
            if entry_id != int(confirm_id):
                return render(request, "editor/actions/delete_entry.html", {"error": "Confirmation failed..."})
            entry.delete()
            return render(request, "editor/actions/delete_success.html")
        case 'GET':
            return render(request, "editor/actions/delete_entry.html", context)
        case _:
            return HttpResponseNotAllowed(['GET', 'POST'])

def new(request):
    return redirect(f"/editor/new/")

def edit(request, entry_id:int):
    return redirect(f"/editor/{entry_id}/")

def view(request, entry_id:int):
    return redirect(f"/explorer/entry/{entry_id}/")