from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm




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
    form_class = PostForm
    template_name = 'New_post.html'
    #fields = '__all__'
    #fields = ('title','author','body')

class Update_Post(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit-post.html'
    #fields = '__all__'
    #fields = ('title','body')    
