from django.contrib import admin
from django.urls import path
from Entries import views

urls = [
    path('<int:entry_id>/', views.editor.editor, name='editor/edit_entry'),
    path('new/', views.editor.editor, name='editor/new_entry'),
    path('enter_key/', views.editor.enter_key, name='enter_key'),
    path('enter_key/<str:key>', views.editor.enter_key, name='enter_key'),
    path('partial/custom_field/', views.editor.custom_field, name='custom_field'),
]