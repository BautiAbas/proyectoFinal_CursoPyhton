from django.urls import path
from . import views

urlpatterns = [
    path('vista-general/',views.pantallaUsuarios,name="pantallaUsuarios"),
    path('crear-usuario/',views.crearUsuario,name="crearUsuario"),
]
