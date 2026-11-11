from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('platillos/', views.platillos, name='platillos'),
    path('menu/', views.menu_pdf, name='menu_pdf'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('reservaciones/', views.vista_reservaciones, name='reservaciones'),
    path('resenas/', views.resenas, name='resenas'),
]