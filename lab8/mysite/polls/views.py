from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from polls.forms import RegistrationUsersForm, AuthorizationUsersForm


def index(request):
    return render(request, 'polls/index.html')


def about(request):
    return render(request, 'polls/about.html')


class RegisterUser(CreateView):
    form_class = RegistrationUsersForm
    template_name = 'polls/registration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthorizationUsersForm
    template_name = 'polls/authorization.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return render(request, 'polls/index.html')
