from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import EndUsers


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        EndUsers.objects.create(user=instance)
        print("Profile Craeted")


@receiver(post_save, sender=User)
def update_user(sender, instance, created, **kwargs):
    if not created:
        instance.endusers.save()
        print("Profile updated")
