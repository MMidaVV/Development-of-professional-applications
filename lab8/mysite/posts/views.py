from django.shortcuts import render, redirect
from .models import Likes
from .models import Users
from .models import Images
from .models import Subscribes
from .models import Posts
from .forms import UsersForm, PostsForm, LikesForm, SubscribesForm, ImagesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def posts_home(request):
    posts = Posts.objects.all()
    users = Users.objects.all()
    images = Images.objects.all()
    subscribes = Subscribes.objects.all()
    likes = Likes.objects.all()
    return render(request, 'posts/posts_home.html', {'users': users, 'posts': posts, 'likes': likes,
                                                     'subscribes': subscribes, 'images': images})


class UsersDetailView(DetailView):
    model = Users
    template_name = 'posts/users_view.html'
    context_object_name = 'users'


class PostsDetailView(DetailView):
    model = Posts
    template_name = 'posts/posts_view.html'
    context_object_name = 'posts'


class LikesDetailView(DetailView):
    model = Likes
    template_name = 'posts/likes_view.html'
    context_object_name = 'likes'


class SubscribesDetailView(DetailView):
    model = Subscribes
    template_name = 'posts/subscribes_view.html'
    context_object_name = 'subscribes'


class ImagesDetailView(DetailView):
    model = Images
    template_name = 'posts/images_view.html'
    context_object_name = 'images'


class UsersUpdateView(UpdateView):
    model = Users
    template_name = 'posts/users_update.html'
    form_class = UsersForm


class PostsUpdateView(UpdateView):
    model = Posts
    template_name = 'posts/posts_update.html'
    form_class = PostsForm


class LikesUpdateView(UpdateView):
    model = Likes
    template_name = 'posts/likes_update.html'
    form_class = LikesForm


class SubscribesUpdateView(UpdateView):
    model = Subscribes
    template_name = 'posts/subscribes_update.html'
    form_class = SubscribesForm


class ImagesUpdateView(UpdateView):
    model = Images
    template_name = 'posts/images_update.html'
    form_class = ImagesForm


class UsersDeleteView(DeleteView):
    model = Users
    success_url ='/posts/'
    template_name = 'posts/users_delete.html'


class PostsDeleteView(DeleteView):
    model = Posts
    success_url ='/posts/'
    template_name = 'posts/posts_delete.html'


class LikesDeleteView(DeleteView):
    model = Likes
    success_url ='/posts/'
    template_name = 'posts/likes_delete.html'


class SubscribesDeleteView(DeleteView):
    model = Subscribes
    success_url ='/posts/'
    template_name = 'posts/subscribes_delete.html'


class ImagesDeleteView(DeleteView):
    model = Images
    success_url ='/posts/'
    template_name = 'posts/images_delete.html'


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


def createPosts(request):
    error = ''
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_home')
        else:
            error = 'Форма была неверной'
    form = PostsForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'posts/createPosts.html', data)


def createLikes(request):
    error = ''
    if request.method == 'POST':
        form = LikesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_home')
        else:
            error = 'Форма была неверной'
    form = LikesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'posts/createLikes.html', data)


def createSubscribes(request):
    error = ''
    if request.method == 'POST':
        form = SubscribesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_home')
        else:
            error = 'Форма была неверной'
    form = SubscribesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'posts/createSubscribes.html', data)


def createImages(request):
    error = ''
    if request.method == 'POST':
        form = ImagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_home')
        else:
            error = 'Форма была неверной'
    form = ImagesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'posts/createImages.html', data)


