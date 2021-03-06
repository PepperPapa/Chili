import re
import datetime
import os

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Article
from .forms import ArticleForm
from Chili.settings import MEDIA_ROOT, BASE_DIR

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
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['article_title']
            content = form.cleaned_data['article_content']
            # print(title, content)
            db_new_article = Article.objects.create(headline = title,
                                                   content = content)
            return HttpResponseRedirect('/articles/' + str(db_new_article.id))
    else:
        return render(request, 'articles/new_article.html')

def edit(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    print(article)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        print(request.method)
        if form.is_valid():
            title = form.cleaned_data['article_title']
            content = form.cleaned_data['article_content']
            # print(title, content)
            article.headline = title
            article.content = content
            article.update_date = datetime.datetime.now()
            article.save()  
            return HttpResponseRedirect('/articles/{0}/'.format(str(article.id)))
    else:
        return render(request, 'articles/edit_article.html', {'article': article})

def detail(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'articles/article_detail.html', {'article': article})

@csrf_exempt
def upload_file(request):
    file_obj = request.FILES.get('file')
    if file_obj:   # 处理附件上传到方法
        file_name = request.POST['key']
        destination = open(os.path.join(BASE_DIR, MEDIA_ROOT, file_name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in file_obj.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        return JsonResponse({'size': 'ok'})