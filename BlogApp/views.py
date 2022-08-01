from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView, DeleteView, DetailView, TemplateView, CreateView, UpdateView

from django.db import models
from django.db.models import Model
from django.http import HttpResponse
from django.contrib.auth.models import User
import datetime
from django.urls import reverse_lazy

class createPage(CreateView):
    model = Post
    template_name='create.html'
    fields= ['title', 'body']
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class updatePost(UpdateView):
    model = Post
    template_name='update.html'
    fields = ['title', 'body']

class deletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/'



class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    model= Post
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'

