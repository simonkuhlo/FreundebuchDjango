from typing import Type, Optional
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from .custom_field_handler import CustomFieldHandler
from .custom_text_field_handler import CustomTextFieldHandler
from Entries.models import EntryV1

custom_field_mapping = {
    "txt" : CustomTextFieldHandler,
}


def get_handler(key:str) -> CustomFieldHandler:
    if key in custom_field_mapping.keys():
        return custom_field_mapping[key]()
    else:
        raise KeyError("Custom field key not found.")

def create(key:str, request:HttpRequest, entry:EntryV1) -> None:
    try:
        handler = get_handler(key)
        handler.create(request, entry)
    finally:
        return

def render_field(key:str, request:HttpRequest, entry:Optional[EntryV1] = None, edit_mode: bool = False) -> HttpResponse:
    try:
        handler = get_handler(key)
    except KeyError:
        return render(request, "book_explorer/parts/custom_fields/not_found.html")
    return handler.get_rendered(request, entry, edit_mode=edit_mode)

def render_field_str(key:str, entry:Optional[EntryV1] = None, edit_mode: bool = False) -> str:
    try:
        handler = get_handler(key)
    except KeyError:
        return render_to_string("book_explorer/parts/custom_fields/not_found.html")
    return handler.get_rendered_str(entry, edit_mode=edit_mode)
