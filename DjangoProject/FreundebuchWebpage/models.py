from django.db import models
from Entries.models import EntryV1

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    preview = models.TextField()
    content = models.TextField()
    pinned = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="blogposts/thumbnails/", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class EntryCustomization(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    public = models.BooleanField(default=False)
    font_color = models.CharField(max_length=20)
    font_style = models.CharField(max_length=20)
    border_color = models.CharField(max_length=20)
    border_width = models.CharField(max_length=20)
    border_style = models.CharField(max_length=100)
    border_radius = models.IntegerField()

    #TODO add validation
    additional_css = models.TextField()
