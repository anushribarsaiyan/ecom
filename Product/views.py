from django.shortcuts import render
from Product.models import Product 

# Create your views here.



def get_product(request, slug):

    try:
        product= Product.objects.get(slug = slug)
        context = {'product':Product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_by_size(size)
        return render(request,'product/product.html',context={'product':product,'updated_price':price,'size':size})

    except Exception as e:
        print(e)

    return render(request,'product/product.html')