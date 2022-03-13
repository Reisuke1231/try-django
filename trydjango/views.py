"""
To render html web pages
"""

from django.http import HttpResponse
import random

name = "Reisuke1231"
number = random.randint(10, 10000000)
HTML_STRING = f"""
<h1>Hello {name} - number:{number}</h1>
"""


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response
    """
    return HttpResponse(HTML_STRING)
