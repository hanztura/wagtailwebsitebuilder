from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .db import SocialMediaAbstractModel


# Create your models here.
class UserProfile(SocialMediaAbstractModel):
    user = models.OneToOneField(
        get_user_model(),
        related_name='custom_profile',
        on_delete=models.CASCADE)


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=get_user_model())
# def save_user_profile(sender, instance, **kwargs):
#     instance.custom_profile.save()
