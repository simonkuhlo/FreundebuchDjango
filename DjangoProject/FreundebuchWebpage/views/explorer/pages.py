from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Entries.models import EntryV1, CreateCode

def book_start(request) -> HttpResponse:
    return render(request, "book_explorer/book.html")

def entry(request, source_id:int) -> HttpResponse:
    entry_object = get_object_or_404(EntryV1, pk=source_id)
    context = {
        "current_entry": entry_object
               }
    return render(request, "book_explorer/view_entry.html", context)