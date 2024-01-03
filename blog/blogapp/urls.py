from django.urls import path, include
from . import views
from .views import Home, article_detail

urlpatterns = [
    #path('', views.home, name='home'),
    path('', Home.as_view(), name='home'),
    path('article/<int:pk>/', article_detail.as_view(), name='article-details'),
] 