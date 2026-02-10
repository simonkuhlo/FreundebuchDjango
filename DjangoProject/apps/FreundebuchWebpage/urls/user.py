from django.urls import path

urls = [
    path('login/', apps.FreundebuchWebpage.views.user.login_page, name='login'),
    path('logout/', apps.FreundebuchWebpage.views.user.logout_page, name='logout'),
    path('register/', apps.FreundebuchWebpage.views.user.register_page, name='register'),
    path('account/', apps.FreundebuchWebpage.views.user.account_page, name='account'),
]