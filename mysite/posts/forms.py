from .models import Users
from django.forms import ModelForm, TextInput, DateInput


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password', 'date_joined']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Имя пользователя'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
            "date_joined": DateInput(attrs={
                'class': 'form-control',
            }),
        }