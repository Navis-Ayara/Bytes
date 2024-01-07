from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class article_detail(DetailView):
    model = Post
    template_name = 'article-details.html'


class Add_Post(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'New_post.html'
    login_url = "/signup/login"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class Update_Post(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit-post.html'
    login_url = "/signup/login"


class Delete_Post(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete-post.html'
    login_url = "/signup/login"
    success_url = reverse_lazy('home')
    redirct_field_name = 'home'

@login_required
def logout_view(request):
  logout(request)
  return redirect('home')