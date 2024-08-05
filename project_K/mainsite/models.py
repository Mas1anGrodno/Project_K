from django.db import models

# Create your models here.

# Модель Project должна представлять собой проект с полями названия, описания и даты создания.
class Project(models.Model):
    proj_name = models.CharField(max_length=255, unique=True, verbose_name="Название проекта")
    proj_desc = models.TextField(blank=True, verbose_name="Описание задачи")
    proj_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания проекта")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проект"
        ordering = ["proj_create"]

    def __str__(self):
      return self.proj_name
# Модель Task должна представлять собой задачу, принадлежащую определённому проекту, с полями названия, описания, статуса и приоритета.
class Tasks(models.Model):
    
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('in_progress', 'В процессе'),
        ('completed', 'Готово'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]

    task_proj = models.ForeignKey(Project, to_field='proj_name', on_delete=models.CASCADE, related_name='tasks', verbose_name="Проект")
    task_name = models.CharField(max_length=255, verbose_name="Задача")
    task_desc = models.TextField(blank=True, verbose_name="Описание проекта")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус задачи")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium', verbose_name="Приоритет задачи")

    class Meta:
        verbose_name = "Задачи"
        verbose_name_plural = "Задачи"
        ordering = ["priority"]
        
# Don't forget 
# python manage.py makemigrations
# python manage.py migrate

