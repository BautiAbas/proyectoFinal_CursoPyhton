from django.urls import path, include
from .views import inicio

urlpatterns = [
    path('', inicio,name='inicio'),
    path('usuarios/', include('manejoDeUsuarios.urls'))
]