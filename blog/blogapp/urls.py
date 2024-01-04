from django.urls import path, include
from . import views
from .views import Home, article_detail, Add_Post

urlpatterns = [
    #path('', views.home, name='home'),
    path('', Home.as_view(), name='home'),
    path('article/<int:pk>/', article_detail.as_view(), name='article-details'),
    path('add_post/', Add_Post.as_view(), name='New_post'),
] 