from django.db import models
from django.contrib.auth.models import User
from .generate_secret import generate_secret

CUSTOM_FIELD_CHOICES = {
    "txt" : "Text Field",
    "img" : "Image Field",
    "audio" : "Audio Field",
    "video" : "Video Field",
    "canvas" : "Canvas Field",
    "button" : "Button Field",
}

class EntryV1(models.Model):
    ## Meta Information
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    published = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    ## -- Questions --
    name = models.CharField(verbose_name="My name is:", max_length=100)
    nicknames = models.CharField(verbose_name="People also call me:", max_length=500, blank=True, null=True)
    birthday = models.DateField(verbose_name="My birthday is on:", blank=True, null=True)
    size = models.CharField(verbose_name="I am this tall:", max_length=100, blank=True, null=True)
    origin = models.CharField(verbose_name="I am from:", max_length=100, blank=True, null=True)
    location = models.CharField(verbose_name="I live in:", max_length=500, blank=True, null=True)
    contact = models.CharField(verbose_name="How you can reach me:", max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    likes = models.CharField(verbose_name="I really like:", max_length=500, blank=True, null=True)
    dislikes = models.CharField(verbose_name="I really don't like:", max_length=500, blank=True, null=True)
    loveliest_experience = models.CharField(verbose_name="My loveliest experience:", blank=True, null=True)
    craziest_experience = models.CharField(verbose_name="My craziest experience:", blank=True, null=True)
    favorite_food = models.CharField(verbose_name="Food", max_length=500, blank=True, null=True)
    favorite_animal = models.CharField(verbose_name="Animal", max_length=500, blank=True, null=True)
    favorite_book = models.CharField(verbose_name="Book / Literature", max_length=500, blank=True, null=True)
    favorite_movie = models.CharField(verbose_name="Movie / Show", max_length=500, blank=True, null=True)
    favorite_music = models.CharField(verbose_name="Music", max_length=500, blank=True, null=True)
    biggest_idol = models.CharField(verbose_name="My biggest idol:", max_length=500, blank=True, null=True)
    want_to_become = models.CharField(verbose_name="In the future, I want to become...", blank=True, null=True)

    custom_field_mode = models.CharField(max_length=10, choices=CUSTOM_FIELD_CHOICES, null=True, blank=True)

    ## -- Customization --
    font_color = models.CharField(max_length=20, blank=True, null=True)
    font_style = models.CharField(max_length=30, blank=True, null=True)
    border_color = models.CharField(max_length=20, blank=True, null=True)
    border_width = models.IntegerField(blank=True, null=True)
    border_style = models.CharField(max_length=100, blank=True, null=True)
    border_radius = models.IntegerField(blank=True, null=True)
    background_color = models.CharField(max_length=20, blank=True, null=True)
    # TODO add validation
    additional_css = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Entry {self.id} by {self.name}"

class CreateCode(models.Model):
    purpose = models.CharField(max_length=100, default="Unknown")
    secret = models.CharField(max_length=100, default=generate_secret, primary_key=True)

    def __str__(self):
        return f"{self.purpose}"

    def is_valid(self, code:str) -> bool:
        if self.objects.filter(secret=code).first():
            return True
        return False

class CustomTextField(models.Model):
    entry = models.ForeignKey(EntryV1, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)

class CustomImageField(models.Model):
    entry = models.ForeignKey(EntryV1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

class CustomAudioField(models.Model):
    entry = models.ForeignKey(EntryV1, on_delete=models.CASCADE)
    #TODO add validators
    audio = models.FileField(upload_to='uploads/', blank=True, null=True)

class CustomVideoField(models.Model):
    entry = models.ForeignKey(EntryV1, on_delete=models.CASCADE)
    # TODO add validators
    video = models.FileField(upload_to='uploads/', blank=True, null=True)

class CustomCanvasField(models.Model):
    entry = models.ForeignKey(EntryV1, on_delete=models.CASCADE)
    # TODO add validators
    canvas = models.FileField(upload_to='uploads/', blank=True, null=True)

class CustomButtonField(models.Model):
    entry = models.ForeignKey(EntryV1, on_delete=models.CASCADE)
    onclick_url = models.URLField(blank=True, null=True)
    text = models.CharField(blank=True, null=True, max_length=100)
