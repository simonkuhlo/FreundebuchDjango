from typing import Type

from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpRequest
from .custom_field_handler import CustomFieldHandler
from ..models import EntryV1, CustomImageField


class CustomImageFieldHandler(CustomFieldHandler):
    @property
    def template_name(self) -> str:
        return "book_explorer/parts/custom_fields/custom_field_image.html"

    @property
    def model(self) -> Type[models.Model]:
        return CustomImageField

    def create(self, request: HttpRequest, entry: EntryV1) -> None:
        image = request.FILES.get("custom_image")
        if not image:
            raise ValidationError("Image field is required")
        self.model.objects.create(entry=entry, image=image)