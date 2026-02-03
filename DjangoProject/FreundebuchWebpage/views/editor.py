from typing import Optional
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from Entries.models import EntryV1, CreateCode
from Entries.custom_fields import shortcuts
from FreundebuchWebpage.forms.entry_customization_form import EntryCustomizationForm
from FreundebuchWebpage.forms.entry_form import EntryForm


def edit(request, entry_id: int):
    entry = EntryV1.objects.filter(id=entry_id).first()
    if not entry:
        return render(request, "main/status_pages/not_found.html", {"message": "Entry not found..."})
    if request.user != entry.owner:
        return render(request, "main/status_pages/permission_denied.html")
    match request.method:
        case 'POST':
            entry_form = EntryForm(request.POST, request.FILES, instance = entry)
            if not entry_form.is_valid():
                entry.rendered_custom_field = shortcuts.render_field_str(entry.custom_field_mode, entry)
                context = {
                    'entry': entry,
                    "entry_form": entry_form
                }
                return render(request, "editor/editor.html", context=context)
            entry_form.save()
            try:
                return redirect(f"/explorer/entry/{entry.get_previous_by_created().id}")
            except:
                return redirect(f"/explorer/entry/first")
        case 'GET':
            entry.rendered_custom_field = shortcuts.render_field_str(entry.custom_field_mode, entry)
            entry_form = EntryForm(instance = entry)
            customization_form = EntryCustomizationForm()
            context = {
                'entry': entry,
                "entry_form" : entry_form,
                "customization_form" : customization_form
            }
            return render(request, "editor/editor.html", context=context)
        case _:
            return HttpResponseNotAllowed(['GET', 'POST'])

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



