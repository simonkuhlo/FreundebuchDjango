from typing import Type
from django.db import models
from django.http import HttpRequest
from .custom_field_handler import CustomFieldHandler
from ..models import EntryV1, CustomTextField


class CustomTextFieldHandler(CustomFieldHandler):
    @property
    def template_name(self) -> str:
        return "book_explorer/parts/custom_fields/custom_field_text.html"

    @property
    def model(self) -> Type[models.Model]:
        return CustomTextField

    def create(self, request: HttpRequest, entry: EntryV1) -> None:
        custom_text = request.POST["custom_text"]
        if custom_text:
            self.model.objects.update_or_create(entry=entry, text=custom_text)