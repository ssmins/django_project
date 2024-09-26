from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def index(request): 
    article = Article.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'articles/index.html', context)

def create(request): 
    if request.method == 'POST': # 유효성 검사 
        form = ArticleForm(request.POST, request.FILES) 
        if form.is_valid(): 
            article = form.save() 
            return redirect('articles:detail', article.pk) # 다르게 하는 중 ! 확인 
    else: 
        form = ArticleForm()
    context = {
        'form' : form , 
    }
    return render(request, 'articles/create.html', context) # 유효성 검사 실패하면 해당 화면 다시 보여주기 

def detail(request, pk): 
    article = Article.objects.get(pk=pk) 
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context) 

def delete(request, pk): 
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')