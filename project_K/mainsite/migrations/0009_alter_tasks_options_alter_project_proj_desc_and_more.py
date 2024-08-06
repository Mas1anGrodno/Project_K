# Generated by Django 5.0.7 on 2024-08-06 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_rename_auth_user_users_alter_tasks_task_end'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['task_end'], 'verbose_name': 'Задачи', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterField(
            model_name='project',
            name='proj_desc',
            field=models.TextField(blank=True, verbose_name='Описание проекта'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('Ожидает', 'Ожидает'), ('В процесс', 'В процессе'), ('Готово', 'Готово')], default='pending', max_length=20, verbose_name='Статус задачи'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_desc',
            field=models.TextField(blank=True, verbose_name='Описание задачи'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_end',
            field=models.DateField(null=True, verbose_name='Выполнить до'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name='Коментарий')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_coment', to='mainsite.users', verbose_name='Коментарий пользователя')),
            ],
        ),
    ]
