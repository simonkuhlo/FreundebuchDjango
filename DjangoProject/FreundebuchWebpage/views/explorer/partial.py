from unittest import case
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from Entries.models import EntryV1, CustomTextField


def first(request) -> HttpResponse:
    source_entry = EntryV1.objects.first()
    context = {
        "current_entry": source_entry,
        "previous_entry": None,
        "transition": "next",
        "edit_mode": False
    }
    return render(request, "book_explorer/parts/animated_entry.html", context)

def next_entry(request, source_id: int) -> HttpResponse:
    source_entry = EntryV1.objects.filter(pk=source_id).first()
    if source_entry:
        source_entry.rendered_custom_field = get_custom_field(source_entry.id)
        try:
            current_entry = source_entry.get_next_by_created()
            current_entry.rendered_custom_field = get_custom_field(current_entry.id)
        except EntryV1.DoesNotExist:
            current_entry = None
    else:
        current_entry = EntryV1.objects.first()
    context = {
        "current_entry": current_entry,
        "previous_entry": source_entry,
        "transition": "next",
        "edit_mode": False
               }
    return render(request, "book_explorer/parts/animated_entry.html", context)


def previous_entry(request, source_id: int) -> HttpResponse:
    source_entry = EntryV1.objects.filter(pk=source_id).first()
    if source_entry:
        source_entry.rendered_custom_field = get_custom_field(source_entry.id)
        try:
            previous_entry_object = source_entry.get_previous_by_created()
            previous_entry_object.rendered_custom_field = get_custom_field(previous_entry_object.id)
        except EntryV1.DoesNotExist:
            previous_entry_object = None
    else:
        previous_entry_object = EntryV1.objects.first()
    context = {
        "current_entry": source_entry,
        "previous_entry": previous_entry_object,
        "transition" : "prev",
        "edit_mode" : False
    }
    return render(request, "book_explorer/parts/animated_entry.html", context)

def get_custom_field(entry_id:int) -> str:
    entry = EntryV1.objects.filter(pk=entry_id).first()
    if not entry:
        return ""
    match entry.custom_field_mode:
        case "txt":
            custom_text_object = CustomTextField.objects.filter(entry=entry).first()
            if custom_text_object:
                custom_text = custom_text_object.text
            else:
                custom_text = ""
            return render_to_string("book_explorer/parts/custom_fields/custom_field_text.html", {"custom_text" : custom_text})
        case _:
            return ""