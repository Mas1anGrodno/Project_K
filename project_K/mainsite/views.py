from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework import serializers
from .serializers import *
from mainsite.models import *
from .forms import *

# Create your views here.

def home(request):
    
    context = {
        'title': 'Главная страница',
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Главная страница"
        }

    return render(request, 'project_K/home.html',context)

def proj(request):
    projects = Project.objects.all()
    
    context = {
        'title': 'Все проекты',
        'projects': projects,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header': "Все Проекты"
        }
    return render(request, 'project_K/proj.html',context)


def coments(request, coment_id):
    all_coments = Comments.objects.filter(comment_task_id=coment_id)
    context = {
        'title': 'Просмотр Коментариев',
        'all_coments': all_coments,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Просмотр Коментариев"
    }

    return render(request, 'project_K/coments.html', context)

@login_required
def add_coment(request):
    if request.method == 'POST':
        form = ComentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_name = request.user
            comment.save()
            return HttpResponseRedirect('/')
        else:
            form.add_error(None, 'Ошибка при добавлении комментария')
    else:
        form = ComentsForm()

    context = {
        'title': 'Добавление Коментария',
        'form': form,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Добавление Коментария"
    }
    return render(request, 'project_K/add_coment.html', context)

def tasks(request):
    tasks = Tasks.objects.all()

    context = {
        'title': 'Все задачи',
        'tasks': tasks,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Все Задачи"
        }
    return render(request, 'project_K/tasks.html',context)

@login_required
def view_task(request, task_id):
    instance = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            task = form.save(commit=False)
            task.sender = request.user
            task.save()
            return HttpResponseRedirect('/tasks')
        else:
            form.add_error(None, 'Ошибка при редактировании задачи')
    else:
        form = TaskForm(instance=instance)

    context = {
        'title': 'Просмотр задачи',
        'form': form,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Просмотр задачи"
    }
    return render(request, 'project_K/viewtask.html', context)

@login_required
def add_proj(request):

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
        'form': form,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Добавление проекта"
    }
    return render(request, 'project_K/add_proj.html', context)

@login_required
def add_task(request):    
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.sender = request.user
            task.save()
            return HttpResponseRedirect('/tasks')
        else:
            form.add_error(None, 'Ошибка при добавлении задачи')
    else:
        form = AddTask()
    
    context = {
        'title': 'Добавление задачи',
        'form': form,
        'footer' : "(c) Максим-Ка - Email: example@example.com",
        'header' : "Добавление задачи"
    }
    return render(request, 'project_K/add_task.html', context)

class TasksAPIView(generics.ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = AllTaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer