from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from Entries.models import EntryV1


def first(request) -> HttpResponse:
    source_entry = EntryV1.objects.first()
    context = {
        "current_entry": source_entry,
        "previous_entry": None,
        "transition": "next",
        "edit_mode": False
    }
    return render(request, "book_explorer/animated_entry.html", context)

def next_entry(request, source_id: int) -> HttpResponse:
    try:
        source_entry = EntryV1.objects.get(pk=source_id)
        current_entry = source_entry.get_next_by_created()
    except EntryV1.DoesNotExist:
        return first(request)
    context = {
        "current_entry": current_entry,
        "previous_entry": source_entry,
        "transition": "next",
        "edit_mode": False
               }
    return render(request, "book_explorer/animated_entry.html", context)


def previous_entry(request, source_id: int) -> HttpResponse:
    try:
        source_entry = EntryV1.objects.get(pk=source_id)
        previous_entry_object = source_entry.get_previous_by_created()
    except EntryV1.DoesNotExist:
        return first(request)
    context = {
        "current_entry": source_entry,
        "previous_entry": previous_entry_object,
        "transition" : "prev",
        "edit_mode" : False
    }
    return render(request, "book_explorer/animated_entry.html", context)