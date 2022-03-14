from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from .forms import ArticleForm
from .models import Article

def search(request):
    query_dict = request.GET
    articles = []

    try:
        query = query_dict.get('q')
        if query:
            articles = Article.objects.filter(Q(title__contains=query) | Q(content__contains=query))
    except Exception as e:
        print(e)

    context = {
        'articles': articles
    }

    return render(request, 'articles/search.html', context=context)

def detail(request, id):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)

    context = {
        'object': article_obj,
    }

    return render(request, 'articles/detail.html', context=context)

@login_required
def create(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form': form
    }
    form = ArticleForm(request.POST)
    context['form'] = form
    if form.is_valid():
        posted = {
            'title': form.cleaned_data.get('title'),
            'content': form.cleaned_data.get('content')
        }
        context['article'] = Article.objects.create(**posted)

    return render(request, 'articles/create.html', context=context)
# def create(request):
#     form = ArticleForm()
#     context = {
#         'form': form
#     }
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             posted = {
#                 'title': form.cleaned_data.get('title'),
#                 'content': form.cleaned_data.get('content')
#             }
#             context['article'] = Article.objects.create(**posted)
# 
#     return render(request, 'articles/create.html', context=context)