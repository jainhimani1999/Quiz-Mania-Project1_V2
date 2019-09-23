from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="Catalog"),
    path("admin_V",views.admin_V,name="admin"),
]