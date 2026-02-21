from django.urls import path
from ..views import pages

app_name = "Pages"

urlpatterns = [
    path('', pages.index, name='index'),
    path('dedication/', pages.dedication, name='dedication'),
]
