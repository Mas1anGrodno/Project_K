from django.db.models.signals import post_save ,post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Tasks


@receiver(post_save, sender=Tasks)
def user_log(sender, instance, created, **kwargs):
    if created:
        print("добавлена задача")

@receiver(post_delete, sender=Tasks)
def user_log(sender, instance, **kwargs):
        print("задача удалена")

@receiver(post_save, sender=User) 
def notify_superuser_creation(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        print(f'User {instance.username} has been created.')