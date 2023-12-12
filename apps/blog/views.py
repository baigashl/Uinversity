from django.shortcuts import render
from .models import News
from django.views import generic


def home(request):
    news = News.objects.all()
    return render(request, 'home.html', {'news_list': news})


class NewsListView(generic.ListView):
    model = News
    template_name = 'home.html'
    context_object_name = 'news_list'


class NewsCreateView(generic.CreateView):
    model = News
    fields = ['title', 'text', 'image']


class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        return context



