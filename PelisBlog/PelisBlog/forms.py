from django.forms import ModelForm, fields, Form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']
        
class RegistroForm(UserCreationForm):
    rut = forms.CharField(label="Rut")
    direccion = forms.CharField(label="Dirección")
    telefono = forms.IntegerField()
    comuna = forms.CharField(label="Comuna")
    region = forms.CharField(label="Región")
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'rut', 'direccion', 'telefono', 'comuna', 'region']