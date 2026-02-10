from django.contrib import admin
from django.urls import path
from FreundebuchWebpage import views

urls = [
    path('', views.explorer.pages.book_start, name='book_start'),
    path('entry/<int:source_id>/', views.explorer.pages.entry, name='view_entry'),
    path('partial/start/', views.explorer.partial.first, name='book_start'),
    path("partial/entry/<int:source_id>/next/", views.explorer.partial.next_entry, name='next_entry'),
    path("partial/entry/<int:source_id>/prev/", views.explorer.partial.previous_entry, name='prev_entry'),
    path("partial/entry/first", views.explorer.partial.first, name='first_entry'),
]