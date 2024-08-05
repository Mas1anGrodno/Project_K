from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from mainsite.models import *
from .forms import AddProject
from .forms import AddTask
# Create your views here.

def home(request):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}, 
            {'title':'Войти','url':'/admin'}]
    context = {
        'title': 'Главная страница',
        'menu': menu,
        'footer' : "(c) Максим-Ка - Email: example@example.com"
        }

    return render(request, 'project_K/home.html',context)

def proj(request):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}, 
            {'title':'Добавить проект','url':'/add_proj'}]
    projects = Project.objects.all()
    
    context = {
        'title': 'Все проекты',
        'menu': menu,
        'projects': projects,
        'footer' : "(c) Максим-Ка - Email: example@example.com"
        }
    

    return render(request, 'project_K/proj.html',context)

def tasks(request):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}, 
            {'title':'Добавить задачу','url':'/add_task'}]
    tasks = Tasks.objects.all()

    context = {
        'title': 'Все задачи',
        'menu': menu,
        'tasks': tasks,
        'footer' : "(c) Максим-Ка - Email: example@example.com"
        }
    return render(request, 'project_K/tasks.html',context)

def add_proj(request):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}]
    
    if request.method == 'POST':
        form = AddProject(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/proj')
            except:
                form.add_error(None, 'Ошибка при добавлении проекта')
    else:
        form = AddProject()
    
    context = {
        'title': 'Добавление проекта',
        'menu': menu,
        'form': form,
        'footer' : "(c) Максим-Ка - Email: example@example.com"
    }
    return render(request, 'project_K/add_proj.html', context)

def add_task(request):
    menu = [{'title':'Главная','url':'/'}, 
            {'title':'Проекты','url':'/proj'}, 
            {'title':'Задачи','url':'/tasks'}]
    
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/tasks')
            except:
                form.add_error(None, 'Ошибка при добавлении задачи')
    else:
        form = AddTask()
    
    context = {
        'title': 'Добавление задачи',
        'menu': menu,
        'form': form,
        'footer' : "(c) Максим-Ка - Email: example@example.com"
    }
    return render(request, 'project_K/add_task.html', context)


