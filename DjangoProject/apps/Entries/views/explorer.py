from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from apps.Entries.models import EntryV1
from apps.Entries.custom_fields import shortcuts


def first(request) -> HttpResponse:
    source_entry = EntryV1.objects.first()
    if source_entry:
        source_entry.rendered_custom_field = shortcuts.render_field_str(source_entry.custom_field_mode, source_entry)
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
        source_entry.rendered_custom_field = shortcuts.render_field_str(source_entry.custom_field_mode, source_entry)
        try:
            current_entry = source_entry.get_next_by_created()
            current_entry.rendered_custom_field = shortcuts.render_field_str(current_entry.custom_field_mode, current_entry)
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
        source_entry.rendered_custom_field = shortcuts.render_field_str(source_entry.custom_field_mode, source_entry)
        try:
            previous_entry_object = source_entry.get_previous_by_created()
            previous_entry_object.rendered_custom_field = shortcuts.render_field_str(previous_entry_object.custom_field_mode, previous_entry_object)
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

def book_start(request) -> HttpResponse:
    return render(request, "book_explorer/book.html")

def entry(request, source_id:int) -> HttpResponse:
    entry_object = get_object_or_404(EntryV1, pk=source_id)
    entry_object.rendered_custom_field = shortcuts.render_field_str(entry_object.custom_field_mode, entry_object)
    context = {
        "current_entry": entry_object
               }
    return render(request, "book_explorer/view_entry.html", context)