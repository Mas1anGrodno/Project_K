from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=255,unique=True, verbose_name="Имя Пользователя")
    email = models.EmailField(max_length = 255, verbose_name="Электронная почта")
    password = models.CharField(max_length=255, verbose_name="Пароль")
    date_joined = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователь"
        ordering = ["-date_joined"]
    def __str__(self):
      return self.username
    
class Project(models.Model):
    proj_name = models.CharField(max_length=255, unique=True, verbose_name="Название проекта")
    proj_desc = models.TextField(blank=True, verbose_name="Описание проекта")
    proj_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания проекта")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проект"
        ordering = ["proj_create"]

    def __str__(self):
      return self.proj_name

class Tasks(models.Model):
    
    STATUS_CHOICES = [
        ('Ожидает', 'Ожидает'),
        ('В процессе', 'В процессе'),
        ('Готово', 'Готово'),
    ]
    PRIORITY_CHOICES = [
        ('Низкий', 'Низкий'),
        ('Средний', 'Средний'),
        ('Высокий', 'Высокий'),
    ]

    task_proj = models.ForeignKey(Project, to_field='proj_name', on_delete=models.CASCADE, related_name='tasks', verbose_name="Проект")
    implementer = models.ForeignKey(Users, to_field='username',null = True ,on_delete=models.CASCADE, related_name='user', verbose_name="Пользователь" )
    task_name = models.CharField(max_length=255, verbose_name="Задача")
    task_desc = models.TextField(blank=True, verbose_name="Описание задачи")
    task_end = models.DateField(null = True, verbose_name="Выполнить до")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус задачи")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium', verbose_name="Приоритет задачи")
   
    class Meta:
        verbose_name = "Задачи"
        verbose_name_plural = "Задачи"
        ordering = ["task_end"]

    def __str__(self):
      return self.task_name

class Comments(models.Model):
    comment_name = models.ForeignKey(Users, to_field='username',null = True ,on_delete=models.CASCADE, related_name='user_coment', verbose_name="Коментарий пользователя" )
    comment_task = models.ForeignKey(Tasks, to_field='id',on_delete=models.CASCADE, related_name='task_coment', verbose_name="Коментарий задачи" )
    comment = models.TextField(blank=True, verbose_name="Коментарий")
    comment_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания коментария")
    class Meta:
        verbose_name = "Коментарии"
        verbose_name_plural = "Коментарии"
        ordering = ["-comment_create"]

    
# Don't forget 1
# python manage.py makemigrations
# python manage.py migrate

