from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import models, forms

def index(request):
    return render(request, 'post/index.html')

def post_list(request):
    posts = models.Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})