from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import News, Category, Comment
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    news = News.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        'home.html',
        context={
            'news_list': news,
            'category_list': categories,
        }
    )


def filter_by_category(request, id):
    objects = News.objects.filter(category_id=id)
    categories = Category.objects.all()
    return render(request, 'home.html', context={
            'news_list': objects,
            'category_list': categories,
        }
    )


class NewsCreateView(LoginRequiredMixin, generic.CreateView):
    model = News
    fields = ['title', 'text', 'image', 'category']
    template_name = 'news/news_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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


def contact(request):
    return render(request, 'contact.html')


def news_detail(request, pk):
    last_news = News.objects.order_by('-created_date')
    object = News.objects.get(id=pk)
    categories = Category.objects.all()
    comments = Comment.objects.filter(news_id=pk)
    category_count = []
    for category in categories:
        asd = {}
        new = News.objects.filter(category_id=category.id)
        asd['id'] = category.id
        asd['name'] = category.name
        asd['count'] = new.count()
        category_count.append(asd)
    if request.method == 'POST':
        comment = Comment.objects.create(
            user_id=request.user.id,
            news_id=pk,
            text=request.POST['text']
        )
        comment.save()
        return redirect('news-detail', pk)
    return render(request, 'news/news_detail.html', {
        'object': object,
        'comments': comments,
        'last_news': last_news[:3],
        'categories': category_count,
    })





