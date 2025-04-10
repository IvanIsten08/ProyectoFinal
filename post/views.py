from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import models, forms
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView

def index(request):
    return render(request, 'post/index.html')

def post_list(request):
    posts = models.Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})

class PostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    success_url = reverse_lazy('post:post_list')

class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post/post_detail.html'

class PostUpdateView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    success_url = reverse_lazy('post:post_list')
    
class PostDeleteView(DeleteView):
    model = models.Post
    success_url = reverse_lazy('post:post_list')