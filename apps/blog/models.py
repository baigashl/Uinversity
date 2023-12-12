from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    text = models.TextField()
    image = models.ImageField(default='news_default.jpeg', upload_to='news_images')
    created_date = models.DateTimeField()


