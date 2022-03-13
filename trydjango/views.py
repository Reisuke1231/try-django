"""
To render html web pages
"""

from django.http import HttpResponse
import random

from articles.models import Article

random_id = random.randint(1, 4)

article_obj = Article.objects.get(id=random_id)

HTML_STRING = f"""
<h1>{article_obj.title} - id:{article_obj.id}</h1>
"""


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response
    """
    return HttpResponse(HTML_STRING)
