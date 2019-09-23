from django.shortcuts import render,reverse
from django.http import Http404,HttpResponseRedirect,HttpResponse  
from django.contrib.auth import authenticate,login,logout 
from http import cookies 
from django.contrib.auth.models import User 

# Create your views here.
global c
c = cookies.SimpleCookie()
#this is to open the login and registeration page when user comes on website first time
def login_reg(request):
    if  not request.user.is_authenticated:
        return render(request,'index.html') # if user is not logged in open login form
    else:
        return render(request,'Catalog.html',c) # if user is logged in and again redirects to base url then show main catalog page

# this is to extract user data from registration form
def register(request):
    firstname  = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    confirmpassword = request.POST['confirmpassword']
    if password == confirmpassword: 
        # adding the user details inside the database(default user database is being used)
        user = User.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save()

        # need to add a middle page or something which shows that Registration is Successful

        return render(request,"index.html") # after registration,send the user back to login page
    else:
        # need to work in this area that if user enters incorrect password then just prompt them for it
        raise Http404("Oops you entered incorrect password") # It gives a error page which tells if user has entered incorrect password

# this is to check the user has entered valid credentials while log in
def login_check(request):
    # fetch the email and password to check login credentials
    email = request.POST['email']  
    password = request.POST['password']

    # checks the credentials using default authenticate function
    user = authenticate(request,username=email,password=password)

    if user is not None: # user gets some value if user enters valid credentials
        login(request,user)  # creates a session for the user

        # time to set cookies using cookies module
        # set the cookie based on email only
        c = cookies.SimpleCookie()
        c['User_Name'] = email
        c['User_Name']['path'] = '/'
        c['Email'] = email
        c['Email']['path'] = '/'
        return HttpResponseRedirect('/login_reg') # c is send to Catalog page which are set by JS in Catalog.html page

    else:
        return render(request,"index.html")  # open login page if user enters invalid credentials

# this is to delete cookies of user when log out
def logout_check(request):
    logout(request) # deletes the session of the user
    # as soon as user is logged out open the index page again
    if not request.user.is_authenticated:  # to check if session for user has been terminated successfully
            return HttpResponseRedirect(reverse('login_page'))
