from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NuevoPostForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField (max_length=50)
    autor = forms.CharField(max_length=50)
    fecha = forms.DateTimeField(widget=forms.DateInput( attrs={'placeholder': '__/__/____'}))
    resenia = forms.CharField(max_length=200)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    imagen_avatar = forms.ImageField(required=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts={k:"" for k in fields}