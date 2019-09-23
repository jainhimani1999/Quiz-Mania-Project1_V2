from django.urls import path
from . import views

urlpatterns = [
    path("login_reg",views.login_reg,name="login_page"), # open the login page
    path("register",views.register,name="register"), # once submit is hit in registration form used to fetch and store data of new user
    path("login_check",views.login_check,name="logged_in"),  # on login, the authentication of user is done
    path("logout",views.logout_check,name="logged_out"),  # on clicking logout, remove or delete the current user session and take him to login page
]