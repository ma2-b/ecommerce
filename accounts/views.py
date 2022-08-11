from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
