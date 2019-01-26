from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
import re

# Create your views here.
def index(request):
    all_articles = Article.objects.all()
    # TODO:zx 这里随着数据量增加会有性能问题，后续改成生成器模式
    # 把content中的<> </>中的内容全部替换掉，取出一定长度的内容作为summary
    for article in all_articles:
        article.content = re.sub(r'<\/?[a-z]+>', '', article.content)   #替换html tag为空内容
        article.content = re.sub(r'<\s+', ' ', article.content) #多个空格替换为一个空格
        article.content = article.content[:40]
    return render(request, 'articles/index.html', {'all_articles': all_articles})

def new(request):
    return render(request, 'articles/new_article.html')

def edit(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'articles/edit_article.html', {'article': article})

def detail(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'articles/article_detail.html', {'article': article})