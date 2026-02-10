from django.urls import path
from apps.FreundebuchWebpage import views

urls = [
    path('<int:entry_id>/edit/', views.entry.edit, name='edit_entry'),
    path('new/', views.entry.new, name='new_entry'),
    path('<int:entry_id>/delete/', views.entry.delete, name='delete_entry'),
    path('<int:entry_id>/view/', views.entry.view, name='view_entry'),
]