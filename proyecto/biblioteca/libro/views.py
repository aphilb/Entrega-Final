from django.shortcuts import redirect, render
from .forms import AutorForm, LibroForm
from .models import Autor, Libro
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def Home(request):
    return render(request, 'libro/index.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)

            if user is not None:
                login (request, user)
                return render(request, "index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "index.html", {"mensaje":"Error de datos"})
        else:
            return render(request,"index.html", {"mensaje":"Formulario erroneo"})
    form= AuthenticationForm()

    return render(request, "login.html", {'form':form})



def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index.html')
    else:
        autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html',{'autor_form':autor_form})

def listarAutor(request):
    autores = Autor.objects.all()
    return render(request, 'libro/listar_autor.html', {'autores': autores})

def editarAutor(request,id):
    autor_form = None
    error = None
    try:
        autor= Autor.objects.get(id = id)
        if request.method == "GET":
            autor_form= AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance= autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('index.html')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'libro/crear_autor.html', {'autor_form': autor_form, 'error': error})


def eliminarAutor(request, id):
    autor = Autor.objects.get(id=id)
    if request.method == 'POST':
        autor.delete()
        return redirect('libro:listar_autor')
    return render(request,'libro/eliminar_autor.html',{'autor': autor})

def crearLibro(request):
    if request.method == 'POST':
        libro_form = LibroForm(request.POST)
        if libro_form.is_valid():
            libro_form.save()
            return redirect('index.html')
    else:
        libro_form = LibroForm()
    return render(request, 'libro/crear_libro.html',{'libro_form':libro_form})

def listarLibro(request):
    libros = Libro.objects.all()
    return render(request, 'libro/listar_libro.html', {'libro': libros})





