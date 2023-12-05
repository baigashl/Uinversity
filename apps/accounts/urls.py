from django.urls import path

from .views import register, index, login

urlpatterns = [
    path('', index),
    path('register', register, name='register'),
    path('login', login, name='login')
]
