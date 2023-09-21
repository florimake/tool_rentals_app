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
from authentication import views

app_name = "hireman"
urlpatterns = [
    path('', view_home, name="home"),
    path("category/", view_category),
    path("products/", view_products, name="products"),
    path("details/", view_details, name="details"),
    path("home/", view_home, name="home"),
    path("products/<slug>/", view_product_details),
    path("most-popular/<slug>/", view_product_details),
    path("category/<slug>", view_products_category),
    path('test/', lambda _: HttpResponse('MERGE')),
    path("<slug>/client/", view_client_details, name="client_details"),
    path("<slug>/service/", view_service_details, name="service_details"),
    path("client/", view_client_details, name="client_details"),
    path("<slug>/client/contract_details", view_contract_details, name="contract_details"),
    path("<slug>/client/termeni_contract", view_termeni_contract, name="termeni_contract"),
    path("static/hireman/static/media/<poza>", view_imagine, name="view_imagine"),
    path("static/hireman/static/media/category/<poza>", view_imagine, name="view_imagine"),
    path("contracte/", view_db_contracte, name="db_contracte"),
    path("contracte/<pk>", view_contract_preview, name="contract_preview"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]
