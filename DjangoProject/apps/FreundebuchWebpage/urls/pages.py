from django.urls import path

urls = [
    path('', apps.FreundebuchWebpage.views.pages.index, name='index'),
    path('dedication/', apps.FreundebuchWebpage.views.pages.dedication, name='dedication'),
]
