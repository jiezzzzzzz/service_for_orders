from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]