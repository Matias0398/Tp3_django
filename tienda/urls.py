from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar/producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar/cliente/', views.agregar_cliente, name='agregar_cliente'),
]
