from django.urls import path, include
from . import browser, editor, entry, explorer

urlpatterns = [
    path('browser/', include(browser.urls), name='browser'),
    path('editor/', include(editor.urls), name='editor'),
    path('entry/', include(entry.urls), name='entry'),
    path('explorer/', include(explorer.urls), name='explorer'),
]