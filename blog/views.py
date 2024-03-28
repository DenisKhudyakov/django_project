from django.shortcuts import render
from django.views.generic import CreateView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog