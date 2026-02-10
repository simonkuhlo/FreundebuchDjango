from typing import Type
from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpRequest
from .custom_field_handler import CustomFieldHandler
from ..models import EntryV1, CustomCanvasField


class CustomCanvasFieldHandler(CustomFieldHandler):
    @property
    def template_name(self) -> str:
        return "book_explorer/parts/custom_fields/custom_field_canvas.html"

    @property
    def model(self) -> Type[models.Model]:
        return CustomCanvasField

    def create(self, request: HttpRequest, entry: EntryV1) -> None:
        canvas_file = request.FILES['custom_canvas']
        if not canvas_file:
            raise ValidationError("No canvas file provided")
        CustomCanvasField.objects.create(entry=entry, canvas=canvas_file)
