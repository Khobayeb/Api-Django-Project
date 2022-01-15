from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('product/', views.product),
    path('product/<int:pk>/', views.productDetails),
]
