from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path("", home,name='home'),
    path("proj/", proj,name='proj'),
    path("add_proj/", add_proj, name='add_proj'),
    path("tasks/", tasks, name='tasks'),
    path("add_task/", add_task, name='add_task'),
    path("add_coment/", add_coment, name='add_coment'),
    path('viewtask/<int:task_id>/', view_task, name='view_task'),
    path('coments/<int:coment_id>/', coments, name='view_coments'),
    path('api/v1/tasklist/', task_list, name='task-list'),
    path('api/v1/tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('api/v1/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]