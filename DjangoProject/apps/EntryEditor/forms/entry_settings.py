from django.forms import ModelForm, ImageField, FileInput
from apps.Entries.models import EntryV1

class EntrySettingsForm(ModelForm):
    class Meta:
        model = EntryV1
        fields = [
            "published"
        ]