from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(request):
    all_articles = Article.objects.all()
    return render(request, 'articles/index.html', {'all_articles': all_articles})

def new(request):
    return render(request, 'articles/new_article.html')

def detail(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'articles/article_detail.html', {'article': article})