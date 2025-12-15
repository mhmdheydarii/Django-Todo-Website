from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CreatePost
# Create your views here.

class PostListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    ordering = 'id'

class PostCreateView(CreateView):
    model = Post
    form_class = CreatePost
    success_url = '/home/post/'

class PostUpdateView(UpdateView):
    model = Post
    form_class = CreatePost
    success_url = '/home/post/'

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/home/post/'