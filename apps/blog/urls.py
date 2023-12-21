from django.urls import path

from .views import home, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView, contact


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news-delete'),
    path('news/create/', NewsCreateView.as_view(), name='news-create'),
]
