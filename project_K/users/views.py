from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm

# Create your views here.

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}]
    extra_context = {
         'title': 'Авторизация',
         'menu': menu,
         'footer' : "(c) Максим-Ка - Email: example@example.com",
         'header' : "Войти"
     }

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
