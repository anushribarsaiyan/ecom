from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
# from account.models import Profile
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)  
 
        
        if not user_obj.exists():   
            messages.error(request, "Account not found!!")
            return HttpResponseRedirect(request.path_info)
    
        user_obj = authenticate(username= email,password=password)
        
        if not  user_obj[0].Profile.is_email_verifield:
            messages.error(request, "please verifie your account!!")
            return HttpResponseRedirect(request.path_info)


        if user_obj:
            login(request,user_obj)
            return HttpResponseRedirect(request.path_info)
        messages.warning(request,'password is not correct!!!')
        return render(request,'account/login.html')     

    
    return render(request,'account/login.html')



def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)    
        print(user_obj)
        
        if user_obj.exists():   
            messages.error(request, "user already exsit!!")
            return redirect('/register/')
            
        user_obj = User.objects.create(
            first_name = first_name, 
            email=email,
            username = email,
            last_name=last_name,
            password = password)
    
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request,'An email has been sent on your mail')
        return redirect('/register/')
    
    return render(request,'account/register.html')     


