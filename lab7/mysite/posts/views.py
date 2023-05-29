from django.shortcuts import render, redirect
from .models import Likes
from .models import Users
from .models import Images
from .models import Subscribes
from .models import Posts
from .forms import UsersForm
from django.views.generic import DetailView, UpdateView, DeleteView


def posts_home(request):
    posts = Posts.objects.all()
    users = Users.objects.all()
    images = Images.objects.all()
    subscribes = Subscribes.objects.all()
    likes = Likes.objects.all()
    return render(request, 'posts/posts_home.html', {'users': users, 'posts': posts, 'likes': likes, 'subscribes': subscribes, 'images': images})


class NewsDetailView(DetailView):
    model = Users
    template_name = 'posts/details_view.html'
    context_object_name = 'users'


class NewsUpdateView(UpdateView):
    model = Users
    template_name = 'posts/users_update.html'
    form_class = UsersForm


class NewsDeleteView(DetailView):
    model = Users
    success_url ='/users/'
    template_name = 'posts/users_delete.html'



def createUsers(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_home')
        else:
            error = 'Форма была неверной'
    form = UsersForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'posts/createUsers.html', data)