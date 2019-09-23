from django.urls import path
from . import views

urlpatterns = [
    path("login_reg",views.login_reg,name="login_page"),
    path("register",views.register,name="register"),
    path("login_check",views.login_check,name="logged_in"),
    path("logout",views.logout_check,name="logged_out"),
]