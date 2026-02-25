from cssutils import parseString, log
import re
from django.forms import ModelForm, ColorInput, NumberInput, ChoiceField, Select, Textarea
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

SAFE_PROPERTIES = {
    'color', 'background-color', 'border-color', 'font-size', 'font-family',
    'margin', 'padding', 'width', 'height', 'display', 'position', 'top',
    'left', 'right', 'bottom', 'z-index', 'opacity', 'border-style',
    'border-width', 'border-radius', 'box-shadow', 'text-align', 'font-weight'
}

class SafeCSSField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', Textarea(attrs={'class': 'form-control'}))
        super().__init__(*args, **kwargs)

    def clean(self, value):
        value = super().clean(value)
        if not value:
            return ''

        # Disable CSS parser error logging
        log.setLevel(20)  # ERROR level

        try:
            # Parse CSS and extract only safe declarations
            sheet = parseString(value)
            safe_css = self._sanitize_css_rules(sheet)
            return safe_css
        except Exception:
            # Fallback: extract only property-value pairs (very restrictive)
            return self._extract_property_values(value)

    def _sanitize_css_rules(self, sheet):
        """Keep only safe CSS properties and values"""
        safe_css = []

        for rule in sheet:
            if rule.type == rule.STYLE_RULE:
                safe_declarations = []
                for decl in rule.style:
                    prop = decl.name.lower()
                    if prop in SAFE_PROPERTIES:
                        value = decl.value
                        # Basic value sanitization
                        value = self._sanitize_value(value)
                        safe_declarations.append(f"{prop}: {value};")

                if safe_declarations:
                    selector = self._sanitize_selector(str(rule.selector))
                    safe_css.append(f"{selector} {{{' '.join(safe_declarations)}}}")

        return '\n'.join(safe_css)

    def _sanitize_selector(self, selector):
        """Allow only safe selectors"""
        # Strip pseudo-classes/elements and attribute selectors
        selector = re.sub(r'(:|\[).*', '', selector)
        # Only allow simple tag/class/id selectors
        return re.sub(r'[^\w.#]', '', selector)

    def _sanitize_value(self, value):
        """Remove potential breakout attempts from values"""
        # Remove URLs, imports, expressions, etc.
        value = re.sub(r'url\([^)]*\)', 'none', value, flags=re.IGNORECASE)
        value = re.sub(r'expression\([^)]*\)', 'none', value, flags=re.IGNORECASE)
        value = re.sub(r'javascript:', '', value, flags=re.IGNORECASE)
        # Strip quotes that might contain scripts
        value = re.sub(r'"[^"]*?(?<!\\)"', '', value)
        value = re.sub(r"'[^']*?(?<!\\)'", '', value)
        return value.strip()

    def _extract_property_values(self, css_text):
        """Fallback: extract only property-value pairs"""
        # Match simple property: value; declarations
        pattern = r'([a-z\-]+)\s*:\s*([^;]+?)\s*(?:;|\}|$)'
        matches = re.findall(pattern, css_text, re.IGNORECASE)

        safe_props = []
        for prop, val in matches:
            prop = prop.strip().lower()
            if prop in SAFE_PROPERTIES:
                val = self._sanitize_value(val)
                safe_props.append(f"{prop}: {val};")

        return '; '.join(safe_props)


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
    additional_css = SafeCSSField()