from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import BlogModel

# Create your views here.
class BlogListView(ListView):
    model = BlogModel
    template_name = 'home.html'
    # context_object_name = 'blog_list'
    
class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blog_details.html'
    