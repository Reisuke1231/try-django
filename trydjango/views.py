"""
To render html web pages
"""

from http.client import HTTPResponse

HTML_STRING = """
<h1>Hello World</h1>
"""


def home(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response
    """
    return HTML_STRING
