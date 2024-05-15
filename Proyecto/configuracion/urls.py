from django.contrib import admin
from django.urls import path
from aplicacion import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar-producto/', views.buscar_producto, name='buscar_producto'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar-marca/', views.agregar_marca, name='agregar_marca'),
    path('agregar-stock/', views.agregar_stock, name='agregar_stock'),
    path('eliminar-producto/', views.eliminar_producto, name='eliminar_producto'),
    path('eliminar-marca/', views.eliminar_marca, name='eliminar_marca'),
    path('eliminar-stock/', views.eliminar_stock, name='eliminar_stock'),
]
