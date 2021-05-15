from django import dispatch
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from api.models import Film, Series, Online_game, Offline_game
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .managers import CustomUserManager
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    #baskets
    films_basket = models.ManyToManyField(Film)
    series_basket = models.ManyToManyField(Series)
    online_games_basket = models.ManyToManyField(Online_game)
    offline_games_basket = models.ManyToManyField(Offline_game)
    # Bought
    wallet = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


@receiver(pre_save, sender=CustomUser)
def userPreSave(sender, **kwargs):
    print("user is going to be saved")


@receiver(post_save, sender=CustomUser)
def userPostSave(sender, **kwargs):
    print("user is saved")


@receiver(pre_delete, sender=CustomUser)
def userPreDelete(sender, **kwargs):
    print("user is going to be removed")


@receiver(post_delete, sender=CustomUser)
def userPostDelete(sender, **kwargs):
    print("user is removed")


# pre_save.connect(userPreSave, sender=CustomUser, dispatch_uid="userPreSave")
# post_save.connect(userPostSave, sender=CustomUser, dispatch_uid="userPostSave")
# pre_delete.connect(userPreDelete, sender=CustomUser, dispatch_uid="userPreDelete")
# post_delete.connect(userPostDelete, sender=CustomUser, dispatch_uid="userPostDelete")
