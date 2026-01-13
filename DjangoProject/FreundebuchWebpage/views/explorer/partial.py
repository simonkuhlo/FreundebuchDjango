from unittest import case
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from Entries.models import EntryV1, CustomTextField
from Entries import custom_field_mapping


def first(request) -> HttpResponse:
    source_entry = EntryV1.objects.first()
    if source_entry:
        source_entry.rendered_custom_field = custom_field_mapping.render_str_shortcut(source_entry.custom_field_mode, source_entry)
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
        source_entry.rendered_custom_field = custom_field_mapping.render_str_shortcut(source_entry.custom_field_mode, source_entry)
        try:
            current_entry = source_entry.get_next_by_created()
            current_entry.rendered_custom_field = custom_field_mapping.render_str_shortcut(current_entry.custom_field_mode, current_entry)
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
        source_entry.rendered_custom_field = custom_field_mapping.render_str_shortcut(source_entry.custom_field_mode, source_entry)
        try:
            previous_entry_object = source_entry.get_previous_by_created()
            previous_entry_object.rendered_custom_field = custom_field_mapping.render_str_shortcut(previous_entry_object.custom_field_mode, previous_entry_object)
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