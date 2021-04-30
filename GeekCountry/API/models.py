from django.db import models
from API import managers


class Movie_genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    genre = models.ForeignKey(Movie_genre, on_delete=models.CASCADE)
    age_limit = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        abstract = True


class Film(Movie):
    duration = models.FloatField()
    films_manager = managers.Film_manager()


class Series(Movie):
    number_of_movies = models.IntegerField()
    series_manager = managers.Series_manager()


class Game_genre(models.Model):
    name = models.CharField(max_length=100)


class Game(models.Model):
    year = models.IntegerField()
    genre = models.ForeignKey(Game_genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        abstract = True


class Online_game(Game):
    internet_connection = True
    number_of_gamers = models.TextField()
    online_game_manager = managers.Online_game_manager()


class Offline_game(Game):
    internet_connection = False
    offline_game_manager = managers.Offline_game_manager()
