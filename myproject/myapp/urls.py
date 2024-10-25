# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('products/', views.get_products),  # GET method
    path('add_product/', views.add_product),  # POST method
]
