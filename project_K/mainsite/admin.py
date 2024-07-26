from django.contrib import admin
from .models import *

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("proj_name", "proj_create")

admin.site.register(Project, ProjectAdmin)

class TasksAdmin(admin.ModelAdmin):
    list_display = ("task_name", "status", "priority")

admin.site.register(Tasks,TasksAdmin)
