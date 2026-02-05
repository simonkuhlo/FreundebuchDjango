from django.forms import ModelForm, widgets, FileInput, ColorInput
from django.forms.fields import CharField, ImageField

from Entries.models import EntryCustomization

class EntryCustomizationForm(ModelForm):
    class Meta:
        model = EntryCustomization
        fields = [
            "font_color",
            "font_style",
            "border_color",
            "border_width",
            "border_style",
            "border_radius",
            "background_color",
            "additional_css",
        ]
    font_color = CharField(widget=ColorInput(), required=False)
    border_color = CharField(widget=ColorInput(), required=False)
    background_color = CharField(widget=ColorInput(), required=False)