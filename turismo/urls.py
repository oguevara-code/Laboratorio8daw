from django.urls import path
from . import views

urlpatterns = [
    path(
        '', 
        views.lista_destinos,
        name='lista_destinos'
    ),

    path(
        'agregar/',
        views.agregar_destino,
        name='agregar_destino'
    ),

    path(
        'editar/<int:id>/',
        views.editar_destino,
        name='editar_destino'
    ),

    path(
        'eliminar/<int:id>/',
        views.eliminar_destino,
        name='eliminar_destino'
    ),
]