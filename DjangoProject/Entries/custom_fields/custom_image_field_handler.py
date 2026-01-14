from typing import Type
from django.db import models
from django.http import HttpRequest
from .custom_field_handler import CustomFieldHandler
from ..models import EntryV1, CustomTextField


class CustomImageFieldHandler(CustomFieldHandler):
    @property
    def template_name(self) -> str:
        raise NotImplementedError()

    @property
    def model(self) -> Type[models.Model]:
        raise NotImplementedError()

    def create(self, request: HttpRequest, entry: EntryV1) -> None:
        raise NotImplementedError()