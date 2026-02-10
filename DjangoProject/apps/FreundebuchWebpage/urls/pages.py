from django.urls import path
from ..views import pages

urls = [
    path('', pages.index, name='index'),
    path('dedication/', pages.dedication, name='dedication'),
]
