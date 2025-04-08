from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context = {'msj': 'Comienza ahora a publicar tu blog'}
    
    return render(request, 'myapp/index.html', context)

def about(request):
    
    return render(request, 'myapp/about.html')