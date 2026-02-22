from django.urls import path, include
from . import browser, editor, entry, explorer

app_name = "Entries"

urlpatterns = [
    path('browser/', include(browser)),
    path('editor/', include(editor)),
    path('entry/', include(entry)),
    path('explorer/', include(explorer))
]