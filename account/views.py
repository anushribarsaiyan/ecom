from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.


def login_page(request):
    return render(request,'account/login.html')



def register(request):
    try:
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            pasword = request.POST.get('password')

            user_obj = User.objects.filter(username = email)

            if user_obj.exists:
                messages.error(request, "user already exsit!!")
                return HttpResponseRedirect(request.path_info)
            
            user_obj = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email = email,
                password = pasword)
            
            user_obj.set_password()
            user_obj.save()
            messages.warning(request,'An email has been sent on your mail')
            return HttpResponseRedirect(request.path_info)
             
        return render(request,'account/login.html')     
    except Exception as e:
        print(e)   