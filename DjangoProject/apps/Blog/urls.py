from django.urls import path
from . import views

urlpatterns = [
    path('partial/news/', views.news_feed, name='news_feed'),
    path('browser/', views.browser, name='blogposts_browser'),
    path('read/<int:post_id>/', views.reader, name='blogposts_reader'),
]