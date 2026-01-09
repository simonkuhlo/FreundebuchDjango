from django.contrib import admin
from django.urls import path
from .. import views

urls = [
    path('', views.creator.create, name='book_start'),
    path('enter_key/', views.creator.enter_key, name='enter_key'),
    path('enter_key/<str:key>', views.creator.enter_key, name='enter_key'),
    path('partial/custom_field/', views.creator.custom_field, name='custom_field'),
]