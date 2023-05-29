from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, CharField


class RegistrationUsersForm(UserCreationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-input'
            }),
            "password1": PasswordInput(attrs={
                'class': 'form-input'
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-input'
            }),
        }


class AuthorizationUsersForm(AuthenticationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-input'
            }),
            "password1": PasswordInput(attrs={
                'class': 'form-input'
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-input'
            }),
        }

