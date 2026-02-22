from typing import Optional, Type
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from apps.Entries.models import EntryV1
from abc import ABC, abstractmethod


class CustomFieldHandler(ABC):

    @property
    @abstractmethod
    def template_name(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def model(self) -> Type[models.Model]:
        raise NotImplementedError()

    def get_context(self, entry:EntryV1) -> dict:
        db_object = self.model.objects.filter(entry=entry).first()
        return {
            "custom_field_db_object": db_object,
        }

    def get_rendered_str(self, entry:Optional[EntryV1] = None, context:dict = {}, edit_mode:bool = False) -> str:
        if edit_mode:
            context["edit_mode"] = True
        if entry:
            context = context | self.get_context(entry)
        return render_to_string(template_name=self.template_name, context=context)

    def get_rendered(self, request:HttpRequest, entry:Optional[EntryV1] = None, context:dict = {}, edit_mode:bool = False) -> HttpResponse:
        if edit_mode:
            context["edit_mode"] = True
        if entry:
            context = context | self.get_context(entry)
        return render(request, self.template_name, context=context)

    @abstractmethod
    def create(self, request: HttpRequest, entry: EntryV1) -> None:
        raise NotImplementedError()


