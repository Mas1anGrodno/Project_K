from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['task_proj','implementer','implementer','task_name','status','priority' ]