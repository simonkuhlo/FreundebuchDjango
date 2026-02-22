from django.urls import path
from functools import partial
from .. import views

app_name = "Browser"

urlpatterns = [
    path('', views.browser.entry_browser, name="root"),
    path('browser/<int:page>/<int:interval>/', views.browser.entry_browser, name='page'),
    path('browser/last/<int:interval>/', partial(views.browser.entry_browser, page=-1), name='last_page'),
]
