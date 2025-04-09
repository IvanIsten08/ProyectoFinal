from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import LoginForm

def index(request):
    context = {'msj': 'Comienza ahora a publicar tu blog'}
    
    return render(request, 'myapp/index.html', context)

def about(request):
    
    return render(request, 'myapp/about.html')

def MiLoginView(LoginView):
    template_name = 'myapp/login.html'
    authentication_form = LoginForm
    next_page = reverse_lazy('myapp:index')