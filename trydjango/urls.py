from django.contrib import admin
from django.urls import path

from accounts import views as accounts_views
from articles import views as article_views
from .views import home_view

urlpatterns = [
    path('', home_view),
    path('articles/', article_views.search),
    path('articles/<int:id>/', article_views.detail),
    path('articles/create/', article_views.create),
    path('admin/', admin.site.urls),
    path('login/', accounts_views.login),
    path('logout/', accounts_views.logout),
    path('register/', accounts_views.register),
]
