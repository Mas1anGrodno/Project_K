# Generated by Django 5.0.7 on 2024-08-06 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0011_alter_comments_options_comments_comment_create'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-comment_create'], 'verbose_name': 'Коментарии', 'verbose_name_plural': 'Коментарии'},
        ),
    ]
