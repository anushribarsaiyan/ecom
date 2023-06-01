from account.views import *
from django.urls import path



urlpatterns = [
    path('register/',register, name = "register"),
    path('login_page/',login_page, name = "login_page"),
]
