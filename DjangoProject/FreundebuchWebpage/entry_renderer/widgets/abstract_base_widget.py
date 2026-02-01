from abc import ABC, abstractmethod

from django.template.loader import render_to_string


class AbstractBaseWidget(ABC):

    @property
    @abstractmethod
    def template_name(self) -> str:
        raise NotImplementedError()

    def render_str(self):
        context = {"widget" : self}
        return render_to_string(self.template_name, context)