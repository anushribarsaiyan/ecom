from Product.views import get_product
from django.urls import path



urlpatterns = [
    path('<slug>/',get_product, name = "get_product"),
]
