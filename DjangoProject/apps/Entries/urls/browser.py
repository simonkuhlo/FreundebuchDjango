from django.urls import path
from functools import partial

urls = [
    path('browser/', apps.Entries.views.browser.entry_browser, name='browser'),
    path('browser/<int:page>/<int:interval>/', apps.Entries.views.browser.entry_browser, name='browser'),
    path('browser/last/<int:interval>/', partial(apps.Entries.views.browser.entry_browser, page=-1), name='browser'),
]
