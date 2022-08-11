from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from .forms import SingUpForm
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SingUpForm 
    template_name = 'registration/register.html'
    
    def get_success_url(self):
        return reverse('login')