from django.contrib import admin
from django.urls import path
from Entries import views
from functools import partial

urls = [
    path('browser/', views.browser.entry_browser, name='browser'),
    path('browser/<int:page>/<int:interval>/', views.browser.entry_browser, name='browser'),
    path('browser/last/<int:interval>/', partial(views.browser.entry_browser, page=-1), name='browser'),
]
