from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def str(self):
        return str(self.name)
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    def str(self):
        return str(self.name)
    

class Articles(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    tag = models.ManyToManyField(Tag, related_name='tags')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='categories')
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    body = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    on_top = models.BooleanField(default=False)
    comments = models.PositiveBigIntegerField(default=0)
    views = models.PositiveBigIntegerField(default=0)
    
    
    def str(self):
        return str(self.title)
    
class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='post_comments')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    comment = models.TextField()
    
    def str(self):
        return str(self.user.username)