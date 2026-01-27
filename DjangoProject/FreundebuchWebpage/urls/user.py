from django.contrib import admin
from functools import partial
from django.urls import path
from .. import views

urls = [
    path('login/', views.user.login_page, name='login'),
    path('logout/', views.user.logout_page, name='logout'),
    path('register/', views.user.register_page, name='register'),
    path('account/', views.user.account_page, name='account'),
]