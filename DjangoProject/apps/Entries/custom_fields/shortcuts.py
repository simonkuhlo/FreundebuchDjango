from typing import Optional
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .custom_audio_field_handler import CustomAudioFieldHandler
from .custom_field_handler import CustomFieldHandler
from .custom_image_field_handler import CustomImageFieldHandler
from .custom_text_field_handler import CustomTextFieldHandler
from .custom_canvas_field_handler import CustomCanvasFieldHandler
from .custom_button_field_handler import CustomButtonFieldHandler
from .custom_video_field_handler import CustomVideoFieldHandler
from apps.Entries.models import EntryV1
from _project.settings import logger

custom_field_mapping = {
    "txt" : CustomTextFieldHandler,
    "img" : CustomImageFieldHandler,
    "audio" : CustomAudioFieldHandler,
    "canvas" : CustomCanvasFieldHandler,
    "button" : CustomButtonFieldHandler,
    "video" : CustomVideoFieldHandler,
}


def get_handler(key:str) -> CustomFieldHandler:
    if key in custom_field_mapping.keys():
        return custom_field_mapping[key]()
    else:
        raise KeyError("Custom field key not found.")

def create(request:HttpRequest, entry:EntryV1) -> None:
    try:
        handler = get_handler(entry.custom_field_mode)
        handler.create(request, entry)
    except Exception as e:
        logger.log_error(f"Error while creating custom field: {e}")
    finally:
        pass

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
