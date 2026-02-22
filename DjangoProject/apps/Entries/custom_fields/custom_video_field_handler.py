from typing import Type
from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpRequest
from .custom_field_handler import CustomFieldHandler
from ..models import EntryV1, CustomVideoField


class CustomVideoFieldHandler(CustomFieldHandler):
    @property
    def template_name(self) -> str:
        return "book_explorer/parts/custom_fields/custom_field_video.html"

    @property
    def model(self) -> Type[models.Model]:
        return CustomVideoField

    def create(self, request: HttpRequest, entry: EntryV1) -> None:
        video_file = request.FILES['custom_video']
        if not video_file:
            raise ValidationError("No video file provided")
        CustomVideoField.objects.create(entry=entry, video=video_file)