from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('registration', views.RegisterUser.as_view(), name='registration'),
    path('authorization', views.LoginUser.as_view(), name='authorization'),
    path('logout', views.logout_user, name='logout')
]