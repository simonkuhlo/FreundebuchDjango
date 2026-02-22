from django.urls import path
from .. import views

app_name = "Editor"

urlpatterns = [
    path('<int:entry_id>/', views.editor.editor, name='edit_entry'),
    path('new/', views.editor.editor, name='new_entry'),
    path('enter_key/', views.editor.enter_key, name='enter_key'),
    path('enter_key/<str:key>', views.editor.enter_key, name='enter_key_url'),
    path('partial/custom_field/', views.editor.custom_field, name='custom_field'),
]