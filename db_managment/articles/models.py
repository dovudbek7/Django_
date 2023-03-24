from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)


class Aricles(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=100, unique=True)
    tag = models.ManyToManyField(Tag, related_name="tags")
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='categories')
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT)
    body = models.TextField()
    rating = models.models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)
    on_top = models.BooleanField(default=False)
    comments = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT)
    comment = models.TextField()

    def __str__(self):
        return str(self.user.username)
