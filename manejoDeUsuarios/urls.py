from django.urls import path
from . import views

urlpatterns = [
    path('vista-general/',views.pantallaUsuarios,name="pantallaUsuarios"),
    path('crearUsuario',views.crearUsuario,name="crearUsuario"),
]
