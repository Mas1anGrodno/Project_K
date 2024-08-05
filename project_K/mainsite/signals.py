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
def notify_user_creation(sender, instance, created, **kwargs):
    if instance.is_superuser == True:
        print(f"Superuser permissions granted to {instance.username}  --> Superuser status - {instance.is_superuser}")
    elif created :
        print(f"User added - id({instance.id}) {instance.username} Active - {instance.is_active}")
