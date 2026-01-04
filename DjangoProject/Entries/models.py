from django.db import models
from django.contrib.auth.models import User

class EntryV1(models.Model):
    ## Meta Information
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    secret = models.CharField(max_length=100, blank=True, null=True)
    published = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    ## -- Questions --
    # I am...
    name = models.CharField(max_length=100)
    # Others also call me...
    nicknames = models.CharField(max_length=500, blank=True, null=True)
    # My birthday is:
    birthday = models.DateField(blank=True, null=True)
    # I am this tall:
    size = models.CharField(max_length=100, blank=True, null=True)
    #I am from:
    origin = models.CharField(max_length=100, blank=True, null=True)
    # Where I live
    location = models.CharField(max_length=500, blank=True, null=True)
    # How you can contact me (Email, Phone number, Discord)
    contact = models.CharField(max_length=500, blank=True, null=True)
    #image = models.ImageField(upload_to='images/')
    # I really like...
    likes = models.CharField(max_length=500, blank=True, null=True)
    # I really don't like...
    dislikes = models.CharField(max_length=500, blank=True, null=True)
    # My loveliest experience:
    loveliest_experience = models.TextField(blank=True, null=True)
    # My craziest experience:
    craziest_experience = models.TextField(blank=True, null=True)
    # My favorite book:
    favorite_food = models.CharField(max_length=500, blank=True, null=True)
    # My favorite animal:
    favorite_animal = models.CharField(max_length=500, blank=True, null=True)
    # My favorite book:
    favorite_book = models.CharField(max_length=500, blank=True, null=True)
    # My favorite movie:
    favorite_movie = models.CharField(max_length=500, blank=True, null=True)
    # My favorite music:
    favorite_music = models.CharField(max_length=500, blank=True, null=True)
    # I love to do...
    biggest_idol = models.CharField(max_length=500, blank=True, null=True)
    # In the future, I want to become...
    want_to_become = models.TextField(blank=True, null=True)


