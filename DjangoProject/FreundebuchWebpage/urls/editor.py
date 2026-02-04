from django.contrib import admin
from django.urls import path
from .. import views

urls = [
    path('<int:entry_id>/', views.editor.editor, name='editor/edit_entry'),
    path('new/', views.editor.editor, name='editor/new_entry'),
]