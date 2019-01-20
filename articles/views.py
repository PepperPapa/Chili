from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(request):
    all_articles = Article.objects.all()
    return render(request, 'articles/index.html', {'all_articles': all_articles})

def new(request):
    return render(request, 'articles/new_article.html')