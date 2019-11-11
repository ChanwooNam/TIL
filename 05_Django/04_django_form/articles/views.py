import hashlib
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

from .forms import ArticleForm 

from IPython import embed


# Create your views here.
def index(request):
    #embed()
    #if request.user.is_authenticated:
    #    gravatar_url = hashlib.md5(request.user.email.encode('utf-8').lower().strip()).hexdigest()

    #else:
        # 비회원인 경우 null값 
    #    gravatar_url = None 
    
    articles = Article.objects.all()
    #context = {'articles': articles, 'gravatar_url': gravatar_url}
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    # POST 요청 -> 데이터를 받아서 DB에 저장
    if request.method == 'POST':
        # Binding 과정
        # 폼 인스턴스를 생성하고, 전달 받은 데이터를 채운다. 
        # 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다. 
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            # cleaned_data를 통해 딕셔너리 안 데이터를 검증한다. 
            #title = form.cleaned_data.get('title')
            #content = form.cleaned_data.get('content')
            #article = Article.objects.create(title=title, content=content)
            #article.save()

            #----- ModelForm ------
            article = form.save()
        return redirect('articles:detail', article.pk)

    # 사용자에게 폼 보여주기
    else:
        form = ArticleForm()

    # form으로 전달받는 형태가 2가지   
    # 1. GET 요청 -> 비어있는 폼 전달
    # 2. 유효성 검증 실패 -> 에러 메세지를 포함한 채로 폼 전달 
    context = {'form': form}
    return render(request, 'articles/form.html', context)


# 게시글 상세정보를 가져오는 함수
def detail(request, article_pk):
    #article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    context = {'article': article }

    return render(request, 'articles/detail.html', context)

# POST만 들어오게 설정 POST가 아니면 405에러 띄움 
#@login_required  - require_POST와 같이 사용하려면 내부에서 하면됨
@require_POST
def delete(request, article_pk):
    
    if request.user.is_authenticated: #@login_required  - require_POST와 같이 사용하려면 내부에서 하면됨
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()

    #article = get_object_or_404(Article, pk=article_pk)
    #article.delete()
    return redirect('articles:index')
 

@login_required
def update(request, article_pk):

    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        #form = ArticleForm(request.POST)

        #----- ModelForm ------
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            #article.title = form.cleaned_data.get('title')
            #article.content = form.cleaned_data.get('content')
            #article.save()

            #----- ModelForm ------
            article = form.save()

        return redirect('articles:detail', article.pk)
    
    else:
        #form = ArticleForm(initial={
        #    'title': article.title,
        #    'content': article.content,
        #})

        #----- ModelForm ------
        form = ArticleForm(instance=article)

    # 2가지 form 형식
    # 1. GET -> 초기값을 폼에 넣어서 사용자에게 던져줌
    # 2. POST -> is_valid가 False가 리턴됐을 때, 오류 메세지 포함해서 사용자에게 던져줌 
    context = {'form': form}
    return render(request, 'articles/form.html', context)


@require_POST
def comments_create(request, article_pk):

    article = get_object_or_404(Article, pk=article_pk)

    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()

    #if request.method == 'POST':
    #comment_form = CommentForm(request.POST)
    #if comment_form.is_valid():
            # save 메서드 -> 선택 인자 : (기본값) commit=True
            # commit=False : DB에 바로 저장되는 것을 막아준다.
    #    comment = comment_form.save(commit=False)
    #    comment.article = article
    #    comment.save()
            #return redirect('articles:detail', article.pk)
    return redirect('articles:detail', article.pk)


@require_POST
def comments_delete(request, article_pk, comment_pk):

    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()

    #if request.method == "POST":
    #comment = get_object_or_404(Comment, pk=comment_pk)
    #comment.delete()
    
    return redirect('article:detail', article_pk)
