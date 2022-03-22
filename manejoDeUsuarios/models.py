from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    nombreUsuario = models.CharField(max_length=20)
    contraseñaUsuario = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} {self.nombreUsuario}"

class Blog(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    cuerpo = models.CharField(max_length=200)
    autor = models.CharField(max_length=20)
    fechaCreacion = models.DateField()

