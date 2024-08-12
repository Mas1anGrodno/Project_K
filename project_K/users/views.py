from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import LoginUserForm

# Create your views here.

def login_user(request):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}]
           
    
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], 
                                         password=cd['password'],)
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LoginUserForm()
    context = {
        'title': 'Авторизация',
        'menu': menu,
        'form': form,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Войти"
    }
    return render(request, 'users/login.html', context)



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
