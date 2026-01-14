from django.db.models import QuerySet

from ..models import BlogPost

def get_browser(request):
    """Returns the blogpost browser as a HTTPResponse object."""
    pass

def reader(request):
    """Returns the blogpost reader as a HTTPResponse object."""
    pass

def news_feed(request):
    """Returns the blogpost news feed as a HTTPResponse object."""
    context = {"posts" : get_posts()}

def get_posts(start:int = 0, end:int = 5) -> QuerySet[BlogPost, BlogPost]:
    blog_posts = BlogPost.objects.all()[start:end]
    return blog_posts