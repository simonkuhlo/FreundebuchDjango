from django.urls import path
from .. import views

urls = [
    path('<int:entry_id>/edit/', views.entry_crud.edit, name='edit_entry'),
    path('new/', views.entry_crud.new, name='new_entry'),
    path('<int:entry_id>/delete/', views.entry_crud.delete, name='delete_entry'),
    path('<int:entry_id>/view/', views.entry_crud.view, name='view_entry'),
]