from django.shortcuts import render,reverse
from django.http import Http404,HttpResponseRedirect,HttpResponse  
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout 

from http import cookies 
from django.contrib.auth.models import User 
# Create your views here.

#this is to open the login and registeration page when user comes on website first time
def login_reg(request):
    if  not request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return render(request,'Catalog.html')

# this is to extract user data from registration form
def register(request):
    firstname  = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    confirmpassword = request.POST['confirmpassword']
    if password == confirmpassword:
        # adding the user details inside the database
        user = User.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save()

        return render(request,"Catalog.html")
    else:
        raise Http404("Oops you entered incorrect password")
        return render(request,"index.html")
    
# This is to check cookies of user in system, if he /she is logged in or not    
def index(request):
    if not request.user.authenticated:
        return render(request,"index.html",{"message":None})
    context = {
        "user":request.user
    }
    return render(request,"Catalog.html",context)

# this is to check the user has entered valid credentials while log in
def login_check(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request,username=email,password=password)
    if user is not None:
        login(request,user)
        # time to set cookies
        c = cookies.SimpleCookie()
        c['User_Name'] = email
        c['User_Name']['path'] = '/'
        c['Email'] = email
        c['Email']['path'] = '/'
        return render(request,'Catalog.html',c)

    else:
        return render(request,"index.html")

# this is to delete cookies of user when log out
def logout_check(request):
    logout(request)
    if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login_page'))
