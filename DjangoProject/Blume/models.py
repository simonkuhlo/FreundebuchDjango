from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField()

class EntryV1(models.Model):
    ## Meta Information
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    secret = models.CharField(max_length=100)
    published = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    ## -- Questions --
    # I am...
    name = models.CharField(max_length=100)
    # Others also call me...
    nicknames = models.CharField(max_length=500)
    # My birthday is:
    birthday = models.DateField()
    # I am this tall:
    size = models.CharField(max_length=100)
    # Where I live
    location = models.CharField(max_length=500)
    # How you can contact me (Email, Phone number, Discord)
    contact = models.CharField(max_length=500)
    #image = models.ImageField(upload_to='images/')
    # I really like...
    likes = models.CharField(max_length=500)
    # I really don't like...
    dislikes = models.CharField(max_length=500)
    # The best experience I've ever had:
    best_experience = models.TextField()
    # My favorite book:
    favorite_food = models.CharField(max_length=500)
    # My favorite animal:
    favorite_animal = models.CharField(max_length=500)
    # My favorite book:
    favorite_book = models.CharField(max_length=500)
    # My favorite movie:
    favorite_movie = models.CharField(max_length=500)
    # My favorite music:
    favorite_music = models.CharField(max_length=500)
    # I love to do...
    favorite_activity = models.CharField(max_length=500)
    # My biggest dream:
    dream = models.TextField()
    # In the future, I want to become...
    want_to_become = models.TextField()


