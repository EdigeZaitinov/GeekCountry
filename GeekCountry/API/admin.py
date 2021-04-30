from django.contrib import admin
from API.models import Offline_game, Online_game, Game_genre
from API.models import Movie_genre, Film, Series


@admin.register(Movie_genre)  # первый способ
class Movie_genre_admin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Game_genre)  # первый способ
class Game_genre_admin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Film)  # первый способ
class Film_admin(admin.ModelAdmin):
    list_display = ('year', 'country', 'genre', 'name',
                    'age_limit', 'producer', 'description', 'duration')
    list_display_links = ('name',)
    list_filter = ('genre',)
    search_fields = ('genre',)


@admin.register(Series)  # первый способ
class Series_admin(admin.ModelAdmin):
    list_display = ('year', 'country', 'genre', 'name',
                    'age_limit', 'producer', 'description', 'number_of_movies')
    list_display_links = ('name',)
    list_filter = ('genre',)
    search_fields = ('genre',)


@admin.register(Offline_game)  # первый способ
class Offline_game_admin(admin.ModelAdmin):
    list_display = ('year', 'genre', 'name',
                    'description', 'internet_connection')
    list_display_links = ('name',)
    list_filter = ('genre',)
    search_fields = ('genre',)


@admin.register(Online_game)  # первый способ
class Offline_game_admin(admin.ModelAdmin):
    list_display = ('year', 'genre', 'name', 'description',
                    'internet_connection', 'number_of_gamers')
    list_display_links = ('name',)
    list_filter = ('genre',)
    search_fields = ('genre',)

# admin.site.register(Todo,TodoAdmin) второй способ
