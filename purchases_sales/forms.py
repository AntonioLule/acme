#from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django.contrib.auth import password_validation
from django.core.exceptions import ObjectDoesNotExist

# Models
from purchases_sales.models import *


class StoreUserCreationForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': False}), label='Usuario', required=True)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': False}), label='Nombre', required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': False}), label='Apellido', required=True)
    email = forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': False}), label='Email', required=True)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'style': 'text-transform: none;'}),
        label='Contraseña', required=False)
    password2 = forms.CharField(
        widget=forms.PasswordInput(), label='Repita la contaseña', required=False)

    class Meta(UserCreationForm.Meta):
        model = Store_Usr
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')
    