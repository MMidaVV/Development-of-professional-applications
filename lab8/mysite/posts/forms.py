from .models import Users, Posts, Likes, Subscribes, Images
from django.forms import ModelForm, TextInput, DateInput, NumberInput


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password', 'date_joined']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
            "date_joined": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата регистрации'
            }),
        }


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['author_id', 'post', 'like', 'date_created']
        widgets = {
            "author_id": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'id_автора'
            }),
            "post": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пост'
            }),
            "like": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Лайки',
            }),
            "date_created": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выкладывания поста',
            }),
        }


class LikesForm(ModelForm):
    class Meta:
        model = Likes
        fields = ['post', 'user', 'date_like']
        widgets = {
            "post": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пост'
            }),
            "user": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор лайка'
            }),
            "date_like": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата лайка',
            }),
        }


class SubscribesForm(ModelForm):
    class Meta:
        model = Subscribes
        fields = ['follower', 'following', 'date_follow']
        widgets = {
            "follower": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Блогер'
            }),
            "following": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Подписчик'
            }),
            "date_follow": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата подписки',
            }),
        }


class ImagesForm(ModelForm):
    class Meta:
        model = Images
        fields = ['post', 'image']
        widgets = {
            "post": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пост'
            }),
            "image": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на картинку'
            }),
        }



