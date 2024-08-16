from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']

class AllTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['task_proj','implementer','implementer','task_name','status','priority' ]

class TaskSerializer(serializers.ModelSerializer):
    task_proj = serializers.CharField(source='task_proj.proj_name')
    implementer = serializers.CharField(source='implementer.username')
    comments = serializers.SerializerMethodField()
    task_name = serializers.CharField(read_only=False)
    class Meta:
        model = Tasks
        fields = ['task_proj', 'implementer', 'task_name', 'task_end', 'comments']

    def get_comments(self, obj):
        comments = Comments.objects.filter(comment_task=obj)
        return CommentSerializer(comments, many=True).data

class CommentSerializer(serializers.ModelSerializer):
    comment_name = serializers.CharField(source='comment_name.username')

    class Meta:
        model = Comments
        fields = ['comment_name', 'comment']