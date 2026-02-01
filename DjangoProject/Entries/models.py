from django.db import models
from django.contrib.auth.models import User
from . import helpers

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
    secret = models.CharField(max_length=100, blank=True, null=True)
    published = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    ## -- Questions --
    # I am...
    name = models.CharField(verbose_name="My name is:", max_length=100)
    # Others also call me...
    nicknames = models.CharField(verbose_name="People also call me:", max_length=500, blank=True, null=True)
    # My birthday is:
    birthday = models.DateField(verbose_name="My birthday is on:", blank=True, null=True)
    # I am this tall:
    size = models.CharField(verbose_name="I am this tall:", max_length=100, blank=True, null=True)
    #I am from:
    origin = models.CharField(verbose_name="I am from:", max_length=100, blank=True, null=True)
    # Where I live
    location = models.CharField(verbose_name="I live in:", max_length=500, blank=True, null=True)
    # How you can contact me (Email, Phone number, Discord)
    contact = models.CharField(verbose_name="How you can reach me:", max_length=500, blank=True, null=True)
    # Image
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # I really like...
    likes = models.CharField(verbose_name="I really like:", max_length=500, blank=True, null=True)
    # I really don't like...
    dislikes = models.CharField(verbose_name="I really don't like:", max_length=500, blank=True, null=True)
    # My loveliest experience:
    loveliest_experience = models.CharField(verbose_name="My loveliest experience:", blank=True, null=True)
    # My craziest experience:
    craziest_experience = models.CharField(verbose_name="My craziest experience:", blank=True, null=True)
    # My favorite book:
    favorite_food = models.CharField(verbose_name="Food", max_length=500, blank=True, null=True)
    # My favorite animal:
    favorite_animal = models.CharField(verbose_name="Animal", max_length=500, blank=True, null=True)
    # My favorite book:
    favorite_book = models.CharField(verbose_name="Book / Literature", max_length=500, blank=True, null=True)
    # My favorite movie:
    favorite_movie = models.CharField(verbose_name="Movie / Show", max_length=500, blank=True, null=True)
    # My favorite music:
    favorite_music = models.CharField(verbose_name="Music", max_length=500, blank=True, null=True)
    # I love to do...
    biggest_idol = models.CharField(verbose_name="My biggest idol:", max_length=500, blank=True, null=True)
    # In the future, I want to become...
    want_to_become = models.CharField(verbose_name="In the future, I want to become...", blank=True, null=True)

    custom_field_mode = models.CharField(max_length=10, choices=CUSTOM_FIELD_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"Entry {self.id} by {self.name}"

class CreateCode(models.Model):
    purpose = models.CharField(max_length=100, default="Unknown")
    secret = models.CharField(max_length=100, default=helpers.generate_secret, primary_key=True)

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
