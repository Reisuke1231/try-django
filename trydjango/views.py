"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

random_id = random.randint(1, 4)

article_obj = Article.objects.get(id=random_id)
article_queryset = Article.objects.all()

context = {
    'article_list': article_queryset,
    'object': article_obj,
    'title': article_obj.title,
    'id': article_obj.id,
    'content': article_obj.content
}

HTML_STRING = render_to_string('home-view.html', context=context)


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response
    """
    return HttpResponse(HTML_STRING)
