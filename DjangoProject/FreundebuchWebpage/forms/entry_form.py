from django.forms import ModelForm, widgets
from Entries.models import EntryV1


class EntryForm(ModelForm):
    class Meta:
        model = EntryV1
        fields = [
            "name",
            "nicknames",
            "birthday",
            "size",
            "origin",
            "location",
            "contact",
            "image",
            "likes",
            "dislikes",
            "loveliest_experience",
            "craziest_experience",
            "favorite_food",
            "favorite_animal",
            "favorite_book",
            "favorite_movie",
            "favorite_music",
            "biggest_idol",
            "want_to_become",
            "custom_field_mode"
        ]