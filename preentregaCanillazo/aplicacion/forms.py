from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 

class CompradorForm(forms.Form):
    nombre = forms.CharField(max_length=30,required=True,label="Apellido y Nombre")
    domicilio = forms.CharField(max_length=30,required=True,label="Domicilio")
    nro_documento = forms.IntegerField(required=True,label="Número de Documento")

class VendedorForm(forms.Form):
    nombre = forms.CharField(max_length=30,required=True,label="Apellido y Nombre")
    nro_documento = forms.IntegerField(required=True,label="Número de Documento")
    
class ProveedorForm(forms.Form):
    nombre = forms.CharField(max_length=30,required=True,label="Nombre de Proveedor")
    domicilio = forms.CharField(max_length=30,required=True,label="Domicilio")
    nro_cuil = forms.IntegerField(required=True,label="Número de CUIL")

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=30,required=True,label="Nombre de Producto")
    nro_item = forms.IntegerField(required=True,label="Número de Ítem")
    precio = forms.DecimalField(max_digits=10, decimal_places=3, required=True,label="Precio")
    
    
class RegistroForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["first_name","last_name","username", "email", "password1", "password2"]


class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)

    

    
