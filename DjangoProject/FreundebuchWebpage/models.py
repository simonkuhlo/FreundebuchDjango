from django.db import models

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
