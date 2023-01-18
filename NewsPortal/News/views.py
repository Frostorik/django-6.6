from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-date_post'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/new.html'
    context_object_name = 'new'

