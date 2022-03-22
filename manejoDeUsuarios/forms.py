from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    nombreUsuario = forms.CharField(max_length=20)
    contraseñaUsuario = forms.CharField(max_length=30,)

class BlogFormulario(forms.Form):
    titulo = forms.CharField(max_length=20)
    subtitulo = forms.CharField(max_length=20)
    cuerpo = forms.CharField(max_length=200)
    autor = forms.CharField(max_length=20)
    fechaCreacion = forms.DateField()

class BusquedaBlog(forms.Form):
    partialBlog = forms.CharField(label='Buscador',max_length=20)