from django.urls import path

from .views import *


urlpatterns = [
    path("", home,name='home'),
    path("proj/", proj,name='proj'),
    path("add_proj/", add_proj, name='add_proj'),
    path("tasks/", tasks, name='tasks'),
    path("add_task/", add_task, name='add_task'),
    path('viewtask/<int:task_id>/', view_task, name='view_task'),
    
]