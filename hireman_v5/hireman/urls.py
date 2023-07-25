"""hireman_v5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from .views import *

app_name = "hireman"
urlpatterns = [
    path('', view_home, name="home"),
    path("category/", view_category),
    path("products/", view_products, name="products"),
    path("product_details/", view_product_details, name="product_details"),
    path("details/", view_details, name="details"),
    path("home/", view_home, name="home"),
    path("products/<slug>/", view_product_details),
    path("category/<slug>", view_products_category),
    path('test/', lambda _: HttpResponse('MERGE')),
]
