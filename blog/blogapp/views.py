from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post



# Create your views here.
#def home(request):
#   return render(request, 'home.html', {})

class Home(ListView):
    model = Post
    template_name = 'home.html'


class article_detail(DetailView):
    model = Post
    template_name = 'article-details.html'

class Add_Post(CreateView):
    model = Post
    template_name = 'New_post.html'
    fields = '__all__'