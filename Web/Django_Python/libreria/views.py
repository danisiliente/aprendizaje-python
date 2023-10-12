from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def libros(request):
    usuarios = Usuario.objects.all()
    return render(request, 'libros/index.html', {'usuarios': usuarios})
def crear(request):
    formulario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})
def editar(request):
    return render(request, 'libros/editar.html')
