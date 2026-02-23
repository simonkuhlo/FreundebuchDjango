from django.urls import path, include
from . import browser, entry, explorer

app_name = "Entries"

urlpatterns = [
    path('browser/', include(browser)),
    path('entry/', include(entry)),
    path('explorer/', include(explorer))
]