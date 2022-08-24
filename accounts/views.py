from django.urls import reverse, reverse_lazy

from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.views import LoginView
from .forms import SingUpForm
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('market:home')


class UserRegisterView(generic.CreateView):
    form_class = SingUpForm 
    template_name = 'registration/register.html'
    
    def get_success_url(self):
        return reverse('login') 
    