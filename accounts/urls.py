from django.urls import path, include
from . import views

from django.contrib.auth.views import LogoutView


app_name = 'accounts'

urlpatterns = [
    
    path('register/',views.UserRegisterView.as_view(), name='register'),
    path('login/',views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
