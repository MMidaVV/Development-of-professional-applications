from django.shortcuts import render


def index(request):
    return render(request, 'polls/index.html')


def about(request):
    return render(request, 'polls/about.html')