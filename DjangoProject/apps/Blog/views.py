from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost

def browser(request) -> HttpResponse:
    return render(request, "blog_posts/browser.html")

def reader(request, post_id:int) -> HttpResponse:
    blogpost = BlogPost.objects.filter(id=post_id).first()
    context = {"blogpost": blogpost}
    return render(request, "blog_posts/reader.html", context)

def news_feed(request) -> HttpResponse:
    """Returns the blogpost news feed as a HTTPResponse object."""
    blog_posts = BlogPost.objects.all().order_by('-created')[0:10]
    context = {"blog_posts" : blog_posts}
    return render(request, "blog_posts/parts/news_feed.html", context)