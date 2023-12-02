from django.urls import path

from .views import register, index

urlpatterns = [
    path('', index),
    path('register',register)
]
