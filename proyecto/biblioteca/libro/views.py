from django.shortcuts import redirect, render
from .forms import AutorForm, LibroForm
from .models import Autor, Libro
from django.core.exceptions import ObjectDoesNotExist

def Home(request):
    return render(request, 'libro/index.html')

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
            autor_form = AutorForm(request.POST, instance = autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('libro:listar_autor.html')
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
    return render(request, 'libro/listar_libro.html', {'libros': libros})

def editarLibro(request,id):
    libro_form = None
    error = None
    try:
        libro= Libro.objects.get(id = id)
        if request.method == "GET":
            libro_form= LibroForm(instance = libro)
        else:
            libro_form = LibroForm(request.POST, instance= libro)
            if libro_form.is_valid():
                libro_form.save()
            return redirect('index.html')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request,'libro/crear_libro.html', {'libro_form': libro_form, 'error': error})

def eliminarLibro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro:listar_libro')
    return render(request,'libro/eliminar_libro.html',{'libro': libro})