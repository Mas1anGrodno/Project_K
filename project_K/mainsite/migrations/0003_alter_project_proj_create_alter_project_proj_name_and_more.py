# Generated by Django 5.0.7 on 2024-07-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_alter_project_options_alter_tasks_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proj_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания проекта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='proj_name',
            field=models.CharField(max_length=255, verbose_name='Название проекта'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=20, verbose_name='Приоритет задачи'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending', max_length=20, verbose_name='Статус задачи'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_name',
            field=models.CharField(max_length=255, verbose_name='Задача'),
        ),
    ]
