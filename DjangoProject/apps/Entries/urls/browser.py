from django.urls import path
from functools import partial
from .. import views

urls = [
    path('', views.browser.entry_browser, name='browser'),
    path('browser/<int:page>/<int:interval>/', views.browser.entry_browser, name='browser'),
    path('browser/last/<int:interval>/', partial(views.browser.entry_browser, page=-1), name='browser'),
]
