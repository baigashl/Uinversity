from django.urls import path

from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView


urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news-update'),
    path('news/create/', NewsCreateView.as_view(), name='news-create'),
]
