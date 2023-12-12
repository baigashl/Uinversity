from django.urls import path

from .views import home, NewsDetailView


urlpatterns = [
    path('', home, name='home'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
]
