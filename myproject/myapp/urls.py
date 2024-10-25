# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
# GET method
     path('products/', views.product_list),         # List all products or create a new one
    path('products/<str:pk>/', views.product_detail), 
]
