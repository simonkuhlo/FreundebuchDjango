from django.urls import path

urls = [
    path('<int:entry_id>/', apps.Entries.views.editor.editor, name='editor/edit_entry'),
    path('new/', apps.Entries.views.editor.editor, name='editor/new_entry'),
    path('enter_key/', apps.Entries.views.editor.enter_key, name='enter_key'),
    path('enter_key/<str:key>', apps.Entries.views.editor.enter_key, name='enter_key'),
    path('partial/custom_field/', apps.Entries.views.editor.custom_field, name='custom_field'),
]