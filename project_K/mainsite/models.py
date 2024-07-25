from django.db import models

# Create your models here.

# Модель Project должна представлять собой проект с полями названия, описания и даты создания.
class Project(models.Model):
    proj_name = models.CharField(max_length=255)
    proj_desc = models.TextField(blank=True)
    proj_create = models.DateTimeField(auto_now_add=True)

# Модель Task должна представлять собой задачу, принадлежащую определённому проекту, с полями названия, описания, статуса и приоритета.
class Task(models.Model):
    
    #STATUS_CHOICES = [
    #    ('pending', 'Pending'),
    #    ('in_progress', 'In Progress'),
    #    ('completed', 'Completed'),
    #]
    #PRIORITY_CHOICES = [
    #    ('low', 'Low'),
    #    ('medium', 'Medium'),
    #    ('high', 'High'),
    #]

    task_proj = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    task_name = models.CharField(max_length=255)
    task_desc = models.TextField(blank=True)
    task_status = models.CharField(max_length=255)
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    task_proir = models.CharField(max_length=255)
    # priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
