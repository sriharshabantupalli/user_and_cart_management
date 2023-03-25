from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserCartModel, UserProfileModel

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile_and_cart(sender, instance, created, **kwargs):
    if created:
        UserProfileModel.objects.create(owner=instance)
        UserCartModel.objects.create(owner=instance, price=0)