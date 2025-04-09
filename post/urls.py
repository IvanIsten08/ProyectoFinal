from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/list/', views.post_list, name='post_list'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    
]