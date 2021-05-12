from django.db import models


class Film_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_films(self):
        return self.all()

    def get_films_by_genre(self, film_genre):
        return self.filter(genre__name=film_genre)


class Series_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_series(self):
        return self.all()

    def get_series_by_genre(self, series_genre):
        return self.filter(genre__name=series_genre)


class Online_game_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_online_games(self):
        return self.all()

    def get_online_games_by_genre(self, online_game_genre):
        return self.filter(genre__name=online_game_genre)


class Offline_game_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_offline_games(self):
        return self.all()

    def get_offline_games_by_genre(self, offline_game_genre):
        return self.filter(genre__name=offline_game_genre)
