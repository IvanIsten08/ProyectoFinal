from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.views.generic import CreateView

def index(request):
    context = {'msj': 'Comienza ahora a publicar tu blog'}
    
    return render(request, 'myapp/index.html', context)

def about(request):
    
    return render(request, 'myapp/about.html')

class MiLoginView(LoginView):
    template_name = 'myapp/login.html'
    authentication_form = LoginForm
    next_page = reverse_lazy('myapp:index')
    
    def form_valid(self, form):
        usuario = form.get_user()
        if usuario.is_active:
            messages.success(self.request, f'Inicio de sesión exitoso: ¡Bienvenido {usuario.username}!')
        else:
            messages.success(self.request, f'Inicia sesion para iniciar. {usuario.username}!')
        return super().form_valid(form)
    
class MiRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'myapp/register.html'
    success_url = reverse_lazy('myapp:login')
    
    def form_valid(self, form):
        form.instance.is_active = True
        messages.success(self.request, 'Usuario creado correctamente')
        return super().form_valid(form)
    
def profile(request):
    if request.user.is_authenticated:
        context = {'user': request.user}
        return render(request, 'myapp/profile.html', context)
    else:
        messages.error(request, 'Debes iniciar sesión para ver tu perfil')
        return HttpResponse('Debes iniciar sesión para ver tu perfil')
    
def logout_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'Has cerrado sesión correctamente')
        return render(request, 'myapp/index.html')
    else:
        messages.error(request, 'No has iniciado sesión')
        return HttpResponse('No has iniciado sesión')