from typing import Optional
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Entries.models import EntryV1, CreateCode
from Entries.custom_fields import shortcuts
from settings import settings
from ..forms.entry_customization_form import EntryCustomizationForm
from ..forms.entry_form import EntryForm
from ..helpers import can_create_entry


def create(request):
    if not can_create_entry(request):
        return redirect("/creator/enter_key")
    match request.method:
        case "POST":
            custom_field_type = request.POST["custom_field_type"]
            entry_form = EntryForm(request.POST, request.FILES)
            if not entry_form.is_valid():
                print(entry_form.errors)
                return render(request, "editor/editor.html", {"entry_form" : EntryForm()})
            new_entry = entry_form.save()
            if custom_field_type:
                shortcuts.create(custom_field_type, request, new_entry)
            if request.user.is_authenticated:
                new_entry.owner = request.user
                new_entry.save()
            if request.session.exists("code"):
                CreateCode.objects.filter(pk=request.session["code"]).first().delete()
            try:
                return redirect(f"/explorer/entry/{new_entry.get_previous_by_created().id}")
            except:
                return redirect(f"/explorer/entry/first")
        case _:
            context = {
                "customization_form": EntryCustomizationForm(),
                "entry_form" : EntryForm()
            }
            return render(request, "editor/editor.html", context)