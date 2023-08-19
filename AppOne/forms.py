from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class Productosform(forms.ModelForm):
    nombre= forms.CharField()
    categoria= forms.CharField()
    imagen= forms.ImageField()

    class Meta:
        model = Productos
        fields = ['nombre', 'categoria', 'imagen'] 
        widgets = {
            'imagen': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class Serviciosform(forms.Form):
    nombre= forms.CharField()
    categoria= forms.CharField()


class Clientesform(forms.Form):
    nombre= forms.CharField()
    dni= forms.IntegerField()
    email= forms.EmailField()
    fechacompra= forms.DateField()

class UserRegisterForm(UserCreationForm):
    username= forms.CharField()
    email= forms.EmailField()
    password1= forms.CharField(label= 'Contraseña', widget= forms.PasswordInput())
    password2= forms.CharField(label= ' Repita la Contraseña', widget= forms.PasswordInput())

    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        help_texts= { k: '' for k in fields}   

class UserEditForm(UserChangeForm, forms.ModelForm):
    username= forms.CharField(label='Modificar Username')
    email= forms.EmailField(label='Modificar Email')
    password1= forms.CharField(label= 'Modificar Contraseña', widget= forms.PasswordInput())
    password2= forms.CharField(label= ' Repita la Contraseña', widget= forms.PasswordInput())


    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        