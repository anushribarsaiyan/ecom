from account.views import *
from django.urls import path
from home.views import index



urlpatterns = [
    path('home/',index, name = "index"),
   
]