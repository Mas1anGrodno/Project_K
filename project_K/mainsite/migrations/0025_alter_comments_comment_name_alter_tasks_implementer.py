# Generated by Django 5.0.7 on 2024-08-12 18:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0024_alter_comments_comment_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_name',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_coment', to=settings.AUTH_USER_MODEL, verbose_name='Коментарий пользователя'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='implementer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
