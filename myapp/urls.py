from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.MiLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name="myapp/logout.html"), name='logout'),
    path('register/', views.MiRegisterView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
]