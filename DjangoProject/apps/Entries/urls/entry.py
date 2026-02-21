from django.urls import path
from .. import views

app_name = "Entry"

urlpatterns = [
    path('<int:entry_id>/edit/', views.entry_crud.edit, name='edit'),
    path('new/', views.entry_crud.new, name='new'),
    path('<int:entry_id>/delete/', views.entry_crud.delete, name='delete'),
    path('<int:entry_id>/view/', views.entry_crud.view, name='view'),
]