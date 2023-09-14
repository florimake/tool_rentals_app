from django.contrib import admin
from django.urls import path
from . import views
app_name = "registration"

urlpatterns = [
    path("home/", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    
]
