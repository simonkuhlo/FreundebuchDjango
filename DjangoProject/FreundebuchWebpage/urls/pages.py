from django.contrib import admin
from functools import partial
from django.urls import path
from .. import views

urls = [
    path('', views.pages.index, name='index'),
    path('dedication/', views.pages.dedication, name='dedication'),
]
