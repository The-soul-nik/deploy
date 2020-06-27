from django.shortcuts import render
from .models import Article
def homepage(request):
    return render(request, 'anytime/home.html')


def articles(request):
    articles = Article.objects.all()
    return render(request, 'anytime/articles.html', {'articles':articles})
