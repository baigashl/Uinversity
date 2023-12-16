from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register, profile, update_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        success_url='profile'
    ), name='login'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update-profile'),
]
