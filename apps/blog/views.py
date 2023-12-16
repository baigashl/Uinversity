from django.urls import reverse_lazy

from .models import News
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class NewsListView(generic.ListView):
    model = News
    template_name = 'home.html'
    context_object_name = 'news_list'


class NewsCreateView(LoginRequiredMixin, generic.CreateView):
    model = News
    fields = ['title', 'text', 'image']
    template_name = 'news/news_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        return context


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = News
    fields = ['title', 'text', 'image']
    template_name = 'news/news_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        object = self.get_object()
        if self.request.user == object.author:
            return True
        return False


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = News
    template_name = 'news/news_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





