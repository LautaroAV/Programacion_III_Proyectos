from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su usuario'}))
    email = forms.EmailField(label='Correo', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingrese su correo'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingrese su contraseña'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirme su contraseña'}))


