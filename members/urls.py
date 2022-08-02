from django.urls import path
from . import views
from .views import UserRegisterView

app_name = 'members'
urlpatterns = [
    # post views
    path('register/', UserRegisterView.as_view(), name= 'register'),
    path('delete/', views.userDelete, name = 'delete'),

    
]