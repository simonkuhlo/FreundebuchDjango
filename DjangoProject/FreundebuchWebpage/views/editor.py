from typing import Optional
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from Entries.models import EntryV1, CreateCode
from Entries.custom_fields import shortcuts as custom_field_shortcuts
from FreundebuchWebpage.forms.entry_customization_form import EntryCustomizationForm
from FreundebuchWebpage.forms.entry_form import EntryForm
from ..entry_helpers import can_create_entry, can_edit_entry


def editor(request, entry_id: Optional[int] = None):
    entry = EntryV1.objects.filter(id=entry_id).first() if entry_id else None
    if entry:
        if not can_edit_entry(request, entry):
            return render(request, "main/status_pages/permission_denied.html", status=401)
    else:
        if not can_create_entry(request):
            return redirect("/editor/enter_key/", status=401)
    match request.method:
        case 'POST':
            entry_form = EntryForm(request.POST, request.FILES, instance = entry)
            if not entry_form.is_valid():
                entry.rendered_custom_field = custom_field_shortcuts.render_field_str(entry.custom_field_mode, entry)
                context = {
                    'entry': entry,
                    "entry_form": entry_form
                }
                return render(request, "editor/editor.html", context=context)
            entry = entry_form.save()
            if request.user.is_authenticated:
                entry.owner = request.user
            entry.save()
            try:
                return redirect(f"/explorer/entry/{entry.get_previous_by_created().id}/")
            except:
                return redirect(f"/explorer/entry/first/")
        case 'GET':
            if entry:
                entry.rendered_custom_field = custom_field_shortcuts.render_field_str(entry.custom_field_mode, entry)
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

def enter_key(request, key: Optional[str] = None):
    code = key
    match request.method:
        case "GET":
            if not key:
                return render(request, "editor/enter_creation_code.html")
        case "POST":
            code = request.POST.get("code")
        case _:
            return HttpResponse(status=404)
    code_objects = CreateCode.objects.filter(secret=code).first()
    if code_objects:
        request.session["code"] = code
        return redirect("/creator/")
    else:
        context = {"failure" : True}
        return render(request, "editor/enter_creation_code.html", context)

def custom_field(request):
    match request.method:
        case "POST":
            key = request.POST.get("custom_field_select")
            return custom_field_shortcuts.render_field(key, request, edit_mode=True)
        case _:
            return HttpResponse(status=404)