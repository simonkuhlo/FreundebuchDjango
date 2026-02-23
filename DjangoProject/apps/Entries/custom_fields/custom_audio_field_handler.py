from typing import Type
from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpRequest
from .custom_field_handler import CustomFieldHandler
from ..models import EntryV1, CustomAudioField


class CustomAudioFieldHandler(CustomFieldHandler):
    @property
    def template_name(self) -> str:
        return "book/parts/custom_fields/custom_field_audio.html"

    @property
    def model(self) -> Type[models.Model]:
        return CustomAudioField

    def create(self, request: HttpRequest, entry: EntryV1) -> None:
        audio_file = request.FILES['custom_audio']
        if not audio_file:
            raise ValidationError("No audio file provided")
        CustomAudioField.objects.create(entry=entry, audio=audio_file)
