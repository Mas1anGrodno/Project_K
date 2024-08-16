from django.urls import path

from .views import *


urlpatterns = [
    path("", home,name='home'),
    path("proj/", proj,name='proj'),
    path("add_proj/", add_proj, name='add_proj'),
    path("tasks/", tasks, name='tasks'),
    path("add_task/", add_task, name='add_task'),
    path("add_coment/", add_coment, name='add_coment'),
    path('viewtask/<int:task_id>/', view_task, name='view_task'),
    path('coments/<int:coment_id>/', coments, name='view_coments'),
    path('api/v1/tasklist/', TasksAPIView.as_view()),
    #path('api/v1/proj/', ProjComplexView.as_view()),
    path('api/v1/proj/<str:project>/', ProjComplexView.as_view(), name='project-detail'),
]