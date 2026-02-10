from django.shortcuts import render

from django.db.models import QuerySet
from django.shortcuts import render

from .models import BlogPost

def browser(request):
    return render(request, "blog_posts/browser.html")

def reader(request, post_id:int):
    blogpost = BlogPost.objects.filter(id=post_id).first()
    context = {"blogpost": blogpost}
    return render(request, "blog_posts/reader.html", context)

def news_feed(request):
    """Returns the blogpost news feed as a HTTPResponse object."""
    context = {"blog_posts" : get_posts(0, 10)}
    return render(request, "blog_posts/parts/news_feed.html", context)

def get_posts(start:int = 0, end:int = 5) -> QuerySet[BlogPost, BlogPost]:
    blog_posts = BlogPost.objects.all().order_by('-created')[start:end]
    return blog_posts