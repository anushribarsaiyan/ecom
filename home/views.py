from django.shortcuts import render
from Product.models import *
# Create your views here.


def index(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request,'home/index.html',context)