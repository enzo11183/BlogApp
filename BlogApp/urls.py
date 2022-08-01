from django.urls import path
from .views import BlogListView, BlogDetailView, createPage, updatePost, deletePost
from . import views

from django.views.generic import RedirectView

app_name = 'BlogApp'
urlpatterns = [
    # post views
    path('', RedirectView.as_view(url='main'), name='main'),
    path('main/', BlogListView.as_view(), name='blog_list'),
    path('create/', createPage.as_view(), name='create'),
    path('post/<int:pk>/update/', updatePost.as_view(), name = 'update_post'),
    path('post/<int:pk>/delete/', deletePost.as_view(), name = 'delete_post'),
    path('post/<int:pk>/' , BlogDetailView.as_view(), name='blog_detail'),
    
]