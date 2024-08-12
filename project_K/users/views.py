from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
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
    
#    def get_success_url(self) -> str:
#        return reverse('home')

# def login_user(request):
#     menu = [{'title':'Главная','url':'/'}, 
#             {'title':'Проекты','url':'/proj'}, 
#             {'title':'Задачи','url':'/tasks'}]
           
    
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], 
#                                          password=cd['password'],)
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#     else:
#         form = LoginUserForm()
#     context = {
#         'title': 'Авторизация',
#         'menu': menu,
#         'form': form,
#         'footer' : "(c) Максим-Ка - Email: example@example.com",
#         'header' : "Войти"
#     }
#     return render(request, 'users/login.html', context)



def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
