from django.urls import path
from ..views import user

app_name = "User"

urlpatterns = [
    path('login/', user.login_page, name='login'),
    path('logout/', user.logout_page, name='logout'),
    path('register/', user.register_page, name='register'),
    path('account/', user.account_page, name='account'),
]