from django.shortcuts import render

from .models import *
# Create your views here.
# def all_articles_view(request):
#     return render(request, "articles/posts.html")


def all_articles_view(request):
    all_posts = Article.objects.all()
    category = Category.objects.all()
    data = {
        'posts': all_posts,
        'category': all_categories
    }

    return render(request, "articles/posts.html", context=data)


def post_detail(request, pk):
    article = Article.objects.get(id=pk)

    return render(request, 'articles/detail.html', context={"object": article})


def category_list(request, category_slug):
    category = Category.objects.get(name=category_slug)
    articles = Articles.objects.filter(category=category)
    return render(request, 'articles/category_posts.html', context={"posts":articles})
