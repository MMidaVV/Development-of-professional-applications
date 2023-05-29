from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_home, name='posts_home'),
    path('createUsers', views.createUsers, name='createUsers'),
    path('createPosts', views.createPosts, name='createPosts'),
    path('createLikes', views.createLikes, name='createLikes'),
    path('createSubscribes', views.createSubscribes, name='createSubscribes'),
    path('createImages', views.createImages, name='createImages'),
    path('user/<int:pk>', views.UsersDetailView.as_view(), name='users-detail'),
    path('post/<int:pk>', views.PostsDetailView.as_view(), name='posts-detail'),
    path('like/<int:pk>', views.LikesDetailView.as_view(), name='likes-detail'),
    path('subscribe/<int:pk>', views.SubscribesDetailView.as_view(), name='subscribes-detail'),
    path('images/<int:pk>', views.ImagesDetailView.as_view(), name='images-detail'),
    path('user/<int:pk>/update', views.UsersUpdateView.as_view(), name='users-update'),
    path('user/<int:pk>/delete', views.UsersDeleteView.as_view(), name='users-delete'),
    path('post/<int:pk>/update', views.PostsUpdateView.as_view(), name='posts-update'),
    path('post/<int:pk>/delete', views.PostsDeleteView.as_view(), name='posts-delete'),
    path('like/<int:pk>/update', views.LikesUpdateView.as_view(), name='likes-update'),
    path('like/<int:pk>/delete', views.LikesDeleteView.as_view(), name='likes-delete'),
    path('subscribe/<int:pk>/update', views.SubscribesUpdateView.as_view(), name='subscribes-update'),
    path('subscribe/<int:pk>/delete', views.SubscribesDeleteView.as_view(), name='subscribes-delete'),
    path('images/<int:pk>/update', views.ImagesUpdateView.as_view(), name='images-update'),
    path('images/<int:pk>/delete', views.ImagesDeleteView.as_view(), name='images-delete'),
]