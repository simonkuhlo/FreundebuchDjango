from django.contrib import admin
from django.urls import path
from .. import views

urls = [
    path('<int:entry_id>/', views.editor.edit, name='edit_entry'),
    path('<int:entry_id>/delete/', views.editor.delete, name='edit_entry'),
]