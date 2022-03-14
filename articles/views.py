from django.db.models import Q
from django.shortcuts import render
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

def create(request):
    context = {}
    if request.method == 'POST':
        posted = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content')
        }
        context['article'] = Article.objects.create(**posted)

    return render(request, 'articles/create.html', context=context)