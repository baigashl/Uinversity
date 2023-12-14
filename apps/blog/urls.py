from django.urls import path

from .views import home, NewsDetailView, NewsCreateView


urlpatterns = [
    path('', home, name='home'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('news/create/', NewsCreateView.as_view(), name='news-create'),
]
