"""TRent_v2/registration URL Configuration
"""
from django.contrib import admin
from django.urls import path
from .views import *

app_name = "registration"
urlpatterns = [
    path('', home, name="home"),
    path("login/", login, name='login'),
    path('signup/', signup, name="signup"),
    path('forgot-password', forgot_password, name="forgot-password")
]
