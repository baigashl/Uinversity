from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    text = models.TextField()
    image = models.ImageField(default='news_default.jpeg', upload_to='news_images')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}, {self.created_date}'

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})


