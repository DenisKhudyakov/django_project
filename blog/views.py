from django.shortcuts import render
from django.views.generic import CreateView, ListView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog


class BlogListView(ListView):
    model = Blog