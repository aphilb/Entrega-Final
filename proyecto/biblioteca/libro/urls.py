from django.urls import path
from .views import crearAutor, listarAutor, editarAutor,eliminarAutor,crearLibro,listarLibro, login_request

urlpatterns = [
    path('crear_autor/', crearAutor, name='crear_autor'),
    path('listar_autor/', listarAutor, name= 'listar_autor'),
    path('editar_autor/<int:id>', editarAutor, name= 'editar_autor' ),
    path('eliminar_autor/<int:id>', eliminarAutor, name = 'eliminar_autor'),
    path('crear_libro', crearLibro, name = 'crear_libro'),
    path('listar_libro', listarLibro, name= 'listar_libro'),
    path('login', login_request, name = 'Login'),
]