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

    class Meta:
        model = Tasks
        fields = ['task_proj', 'implementer', 'task_name', 'task_end', 'comments']

    def get_comments(self, obj):
        comments = Comments.objects.filter(comment_task=obj)
        return CommentSerializer(comments, many=True).data
    
    def update(self, instance, validated_data):
        instance.task_proj.proj_name = validated_data.get('task_proj', instance.task_proj.proj_name)
        instance.implementer.username = validated_data.get('implementer', instance.implementer.username)
        instance.task_name = validated_data.get('task_name', instance.task_name)
        instance.task_end = validated_data.get('task_end', instance.task_end)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):
    comment_name = serializers.CharField(source='comment_name.username')

    class Meta:
        model = Comments
        fields = ['comment_name', 'comment']