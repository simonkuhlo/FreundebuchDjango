from typing import Type
from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpRequest
from .custom_field_handler import CustomFieldHandler
from ..models import EntryV1, CustomButtonField


class CustomButtonFieldHandler(CustomFieldHandler):
    @property
    def template_name(self) -> str:
        return "book/parts/custom_fields/custom_field_button.html"

    @property
    def model(self) -> Type[models.Model]:
        return CustomButtonField

    def create(self, request: HttpRequest, entry: EntryV1) -> None:
        button_url = request.POST['custom_button_url']
        button_text = request.POST['custom_button_text']
        if not button_url:
            raise ValidationError("No button url provided")
        CustomButtonField.objects.create(entry=entry, onclick_url=button_url, text=button_text)
