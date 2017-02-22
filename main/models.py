from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    verified = models.BooleanField(default=False)
    team = models.ForeignKey('Team',related_name='members', on_delete=models.CASCADE, null=True)

class Team(models.Model):
    name = models.CharField(max_length=20)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
