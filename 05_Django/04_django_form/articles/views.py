import hashlib
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

from .forms import ArticleForm, CommentForm

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

            article = form.save(commit=False)
            article.user = request.user
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

    #context = {'article': article }
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }

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
    if request.user == article.user:
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
    #context = {'form': form}
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article
    }
    return render(request, 'articles/form.html', context)


@require_POST
def comments_create(request, article_pk):

    article = get_object_or_404(Article, pk=article_pk)

    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.article_id = article_pk
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

    # 1. 로그인 여부 확인
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        # 2. 로그인한 사용자와 댓글 작성자가 같을 경우
        if request.user == comment.user:
            comment.delete()
            
    #if request.method == "POST":
    #comment = get_object_or_404(Comment, pk=comment_pk)
    #comment.delete()
    
    return redirect('article:detail', article_pk)


@login_required
def like(request, article_pk):
    # 좋아요 누를 게시글 가져오기
    article = get_object_or_404(Article, pk=article_pk)
    # 현재 접속하고 있는 유저
    user = request.user

    # 현재 게시글을 좋아요 누른 사람 목록에서, 현재 접속한 유저가 있을 경우 -> 좋아요 취소 
    #-------------------------------------
    # ORM 방식
    #if article.like_users.filter(pk=user.pk).exists():
    #    article.like_users.remove(user)

    # python list in 방식 
    if user in article.like_users.all():
        article.like_users.remove(user)
    # --------------------------------------
    
    # 목록에 없을 경우 -> 좋아요 누르기 
    else:
        article.like_users.add(user)
    return redirect('articles:index')

@login_required
def follow(request, article_pk, user_pk):
    # 게시글 작성한 유저
    person = get_object_or_404(get_user_model(), pk=user_pk)
    # 지금 접속하고 있는 유저
    user = request.user

    # 게시글 작성 유저 팔로워 명단에 접속 중인 유저가 있을 경우
    # -> unfollow
    if user in person.followers.all():
        person.followers.remove(user)

    # 목록에 없으면
    # -> follow
    else:
        person.followers.add(user)
    # 게시글 상세정보로 redirect
    return redirect('articles:detail', article_pk)
