from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_create/', views.post_create, name='post_create'),
    
]