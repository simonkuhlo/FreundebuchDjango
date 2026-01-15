from django.contrib import admin
from django.urls import path
from .. import views

urls = [
    path('partial/news/', views.blogposts.news_feed, name='news_feed'),
]