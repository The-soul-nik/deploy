from django.urls import path
from .import views


app_name = 'anytime'


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('articles', views.articles, name='articles')
]
