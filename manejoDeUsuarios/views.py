from django.shortcuts import render, redirect
from manejoDeUsuarios.forms import BusquedaBlog, UsuarioFormulario
from .models import Blog, Usuario
from .forms import UsuarioFormulario, BlogFormulario


# Create your views here.

def pantallaUsuarios(request):
    return render(request,"pantallaUsuarios.html",{})

def busqueda(request):
    blogsBuscados = []
    dato = request.GET.get('partialBlog',None)

    if dato is not None:
        blogsBuscados = Blog.objects.filter(nombre__icontains=dato)
        return render(request,'buscarBlog',{'dato':dato,'blogsBuscados': blogsBuscados})
    else:
        buscador = BusquedaBlog()
        return render(request,)

def crearUsuario(request):
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevoUsuario = Usuario(
                nombre=data['nombre'], 
                nombreUsuario=data['nombreUsuario'],
                contraseñaUsuario=data['contraseñaUsuario']
            )
            nuevoUsuario.save()
        return redirect('inicio')

    formulario = UsuarioFormulario()
    return render(request, 'pantallaUsuarios.html', {'formulario': formulario, 'nuevoUsuario': nuevoUsuario})

