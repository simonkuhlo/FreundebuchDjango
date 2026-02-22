from django.urls import path
from .. import views

app_name = "Explorer"

urlpatterns = [
    path('', views.explorer.book_start, name='book_start'),
    path('entry/<int:source_id>/', views.explorer.entry, name='view_entry'),
    path('partial/start/', views.explorer.first),
    path("partial/entry/<int:source_id>/next/", views.explorer.next_entry, name='next_entry'),
    path("partial/entry/<int:source_id>/prev/", views.explorer.previous_entry, name='prev_entry'),
    path("partial/entry/first", views.explorer.first, name='first_entry'),
]