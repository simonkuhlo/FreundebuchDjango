from typing import Optional, Type

from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import EntryV1, CustomTextField


class CustomFieldHandler:

    def get_template_name(self) -> str:
        raise NotImplementedError()

    def get_model(self) -> Type[models.Model]:
        raise NotImplementedError()

    def get_context(self, entry:EntryV1) -> dict:
        db_object = self.get_model().objects.filter(entry=entry).first()
        return {
            "custom_field_db_object": db_object,
        }

    def get_rendered_str(self, entry:Optional[EntryV1] = None, context:dict = {}, edit_mode:bool = False) -> str:
        if edit_mode:
            context["edit_mode"] = True
        if entry:
            context = context | self.get_context(entry)
        return render_to_string(template_name=self.get_template_name(), context=context)

    def get_rendered(self, request:HttpRequest, entry:Optional[EntryV1] = None, context:dict = {}, edit_mode:bool = False) -> HttpResponse:
        if edit_mode:
            context["edit_mode"] = True
        if entry:
            context = context | self.get_context(entry)
        return render(request, self.get_template_name(), context=context)

    def create(self, request: HttpRequest, entry: EntryV1) -> None:
        raise NotImplementedError()

class CustomTextFieldHandler(CustomFieldHandler):

    def get_template_name(self) -> str:
        return "book_explorer/parts/custom_fields/custom_field_text.html"

    def get_model(self) -> Type[CustomTextField]:
        return CustomTextField

    def create(self, request:HttpRequest, entry:EntryV1) -> None:
        custom_text = request.POST["custom_text"]
        if custom_text:
            self.get_model().objects.update_or_create(entry=entry, text=custom_text)


