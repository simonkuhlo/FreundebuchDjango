from django.urls import path
from . import views

app_name = "Blog"

urlpatterns = [
    path('partial/news/', views.news_feed, name='news_feed'),
    path('browser/', views.browser, name='browser'),
    path('read/<int:post_id>/', views.reader, name='reader'),
]