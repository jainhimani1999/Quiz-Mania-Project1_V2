from django.urls import path
from . import views

urlpatterns = [
    path("login_reg",views.login_reg,name="login_page"),
 
]