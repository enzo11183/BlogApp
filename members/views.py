from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm


# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = NewUserForm
    template_name = 'registration/registration.html'
    success_url = '/members/login'
    

def userDelete(request):
    
    u = request.user
    if u.is_anonymous:
        return render(request, 'registration/error.html')
    else:
        u.delete()
        return render(request, 'registration/userdeleted.html')