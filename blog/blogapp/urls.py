from django.urls import path, include
from . import views
from .views import Home, article_detail, Add_Post, Update_Post, Delete_Post

urlpatterns = [
    #path('', views.home, name='home'),
    path('', Home.as_view(), name='home'),
    path('article/<int:pk>/', article_detail.as_view(), name='article-details'),
    path('add_post/', Add_Post.as_view(), name='New_post'),
    path('edit-post/<int:pk>', Update_Post.as_view(), name='edit-post'),
    path('delete-post/<int:pk>', Delete_Post.as_view(), name='delete-post')
] 
