from django.db import models


class Film_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Series_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Online_game_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Offline_game_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
