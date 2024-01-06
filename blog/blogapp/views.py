from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
#def home(request):
#   return render(request, 'home.html', {})

class Home(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id']
    ordering = ['-post_date']


class article_detail(DetailView):
    model = Post
    template_name = 'article-details.html'
  

class Add_Post(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'New_post.html'
    login_url = "/signup/login"
    #fields = '__all__'
    #fields = ('title','author','body')

class Update_Post(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit-post.html'
    login_url = "/signup/login"
    #fields = '__all__'
    #fields = ('title','body')    

class Delete_Post(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete-post.html'
    login_url = "/signup/login"
    success_url = reverse_lazy('home')
    redirct_field_name = 'home'