from email.policy import default

from django.forms import ModelForm, ColorInput, NumberInput, ChoiceField, Select
from django.forms.fields import CharField, IntegerField

from apps.Entries.models import EntryV1

BORDER_STYLES = [
    ('', 'None'),  # Default empty option
    ('solid', 'Solid'),
    ('dashed', 'Dashed'),
    ('dotted', 'Dotted'),
    ('double', 'Double'),
    ('groove', 'Groove'),
    ('ridge', 'Ridge'),
    ('inset', 'Inset'),
    ('outset', 'Outset'),
    ('none', 'None'),
    ('hidden', 'Hidden'),
]

FONTS = [
    ("none", "Default")
]

class RangeInput(NumberInput):
    input_type = "range"

class SliderIntegerField(IntegerField):
    def __init__(self, *args, **kwargs):

        min_value = kwargs.get("min_value", 0)
        max_value = kwargs.get("max_value", 100)
        step = kwargs.pop("step", 1)

        widget = kwargs.pop("widget", None)
        if widget is None:
            widget = RangeInput(
                attrs={
                "min": min_value,
                "max": max_value,
                "step": step,
                }
            )

        super().__init__(widget=widget, *args, **kwargs)


class EntryCustomizationForm(ModelForm):
    class Meta:
        model = EntryV1
        fields = [
            "font_color",
            "font",
            "question_font_size",
            "answer_font_size",
            "border_color",
            "border_width",
            "border_style",
            "border_radius",
            "background_color",
            "element_background_color",
            "additional_css",
        ]
    font_color = CharField(widget=ColorInput(), required=False)
    font = ChoiceField(choices=FONTS, widget=Select(attrs={'class': 'form-select'}), )
    question_font_size = SliderIntegerField(min_value=1, max_value=30)
    answer_font_size = SliderIntegerField(min_value=1, max_value=30)
    border_width = SliderIntegerField(min_value=0, max_value=10)
    border_style = ChoiceField(choices=BORDER_STYLES,widget=Select(attrs={'class': 'form-select'}),)
    border_radius = SliderIntegerField(min_value=1, max_value=30)
    border_color = CharField(widget=ColorInput(), required=False)
    background_color = CharField(widget=ColorInput(), required=False)
    element_background_color = CharField(widget=ColorInput())