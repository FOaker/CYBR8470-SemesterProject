# import markdown
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from article.models import ArticlePost
from .forms import ArticlePostForm
from django.contrib.auth.models import User


def article_list(request):

        if request.GET.get('order') == 'total_views':
            article_list = ArticlePost.objects.all().order_by('-total_views')
            order = 'total_views'
        else:
            article_list = ArticlePost.objects.all()
            order = 'normal'

        paginator = Paginator(article_list, 3)
        page = request.GET.get('page')
        articles = paginator.get_page(page)

        context = {'articles': articles, 'order': order}

        return render(request, 'article/list.html', context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    # article.body = markdown.markdown(article.body,
    #             extensions=[
    #             #'markdown.extensions.extra',
    #             #'markdown.extensions.codehilite',
    #             ])
    article.total_views += 1
    article.save(update_fields=['total_views'])
    context = {'article': article}
    return render(request, 'article/detail.html', context)


@login_required(login_url='/userprofile/login/')
def article_create(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            new_article.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("The content of the form is incorrect, please fill in again. ")
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)


@login_required(login_url='/userprofile/login/')
def article_safe_delete(request, id):

    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        if request.user != article.author:
            return HttpResponse("Sorry, You can't modify this article")
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("Only allow post requests")


@login_required(login_url='/userprofile/login/')
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    if request.user != article.author:
        return HttpResponse("Sorry, You can't modify this article")
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:article_detail", id=id)
        else:
            return HttpResponse("The content of the form is incorrect, please fill in again.")
    else:
        article_post_form = ArticlePostForm()
        context = { 'article': article, 'article_post_form': article_post_form }
        return render(request, 'article/update.html', context)