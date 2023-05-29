from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_home, name='posts_home'),
    path('createUsers', views.createUsers, name='createUsers'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='posts-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='post-delete'),
]