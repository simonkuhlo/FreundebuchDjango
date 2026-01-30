from django import forms
from Entries.models import EntryV1


class EntryForm(forms.ModelForm):
    class Meta:
        model = EntryV1
        exclude = ('id','owner','secret','published','created','updated')