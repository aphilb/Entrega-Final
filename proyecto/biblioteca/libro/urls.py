from django.urls import path
from libro.views import crearAutor, crearLibro, editarAutor, editarLibro, eliminarAutor, eliminarLibro, listarAutor, listarLibro

urlpatterns = [
    path('crear_autor/', crearAutor, name ='crear_autor'),
    path('listar_autor/', listarAutor, name = 'listar_autor'),
    path('editar_autor/<int:id>', editarAutor, name = 'editar_autor' ),
    path('eliminar_autor/<int:id>', eliminarAutor, name = 'eliminar_autor'),
    path('crear_libro/', crearLibro, name = 'crear_libro'),
    path('listar_libro/', listarLibro, name = 'listar_libro'),
    path('editar_libro/<int:id>', editarLibro, name = "editar_libro"),
    path('eliminar_libro/<int:id>', eliminarLibro, name = 'eliminar_libro'),
]