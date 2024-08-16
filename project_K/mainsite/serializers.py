from rest_framework import serializers
from .models import *

class AllTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['task_proj','implementer','implementer','task_name','status','priority' ]

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['implementer','task_name','status','task_end']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment_name','comment']