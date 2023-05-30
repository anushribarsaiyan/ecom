from account.views import login_page
from django.urls import path



urlpatterns = [
    path('logi/',login_page, name = "login"),
]
