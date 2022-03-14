from django.shortcuts import render
from .models import Article

def detail(request, id):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)

    context = {
        'object': article_obj,
    }

    return render(request, 'articles/detail.html', context=context)