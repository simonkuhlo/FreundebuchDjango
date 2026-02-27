import base64
from typing import Type
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.db import models
from django.http import HttpRequest
from .custom_field_handler import CustomFieldHandler
from ..models import EntryV1, CustomCanvasField


class CustomCanvasFieldHandler(CustomFieldHandler):
    @property
    def template_name(self) -> str:
        return "book/parts/custom_fields/custom_field_canvas.html"

    @property
    def model(self) -> Type[models.Model]:
        return CustomCanvasField

    def create(self, request: HttpRequest, entry: EntryV1) -> None:
        canvas_data = request.POST['canvas_data']
        if not canvas_data:
            raise ValidationError("No canvas data provided")
            # Split header and base64 data
        file_format, imgstr = canvas_data.split(';base64,')
        ext = file_format.split('/')[-1]  # "png", "jpeg", etc.
        file = ContentFile(base64.b64decode(imgstr), name=f"drawing.{ext}")
        CustomCanvasField.objects.create(entry=entry, canvas=file)
