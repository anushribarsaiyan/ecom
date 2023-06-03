from django.shortcuts import render
from Product.models import Product 

# Create your views here.



def get_product(request, slug):
    try:
        product= Product.objects.get(slug = slug)
        return render(request,'product/product.html',context={'product':product})

    except Exception as e:
        pass

    return render(request,'product/product.html')