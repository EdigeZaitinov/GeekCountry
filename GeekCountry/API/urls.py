from django.urls import path
from api import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movieGenres', views.get_movie_genres, name='movieGenres'),
    path('gameGenres', views.get_game_genres, name='gameGenres'),

    ######################### FILMS #################################

    path('films', views.get_films, name='films'),
    path('films/<str:films_genre>',
         views.get_films_by_genre, name='filmsByGenre'),

    ######################### SERIES ################################

    path('series', views.get_series, name='series'),
    path('series/<str:series_genre>',
         views.get_series_by_genre, name='seriesByGenre'),

    ######################### ONLINE_GAMES ##########################

    path('onlineGames', views.get_online_games, name='onlineGames'),
    path('onlineGames/<str:online_games_genre>',
         views.get_online_games_by_genre, name='onlineGamesByGenre'),

    ######################### OFFLINE_GAMES ##########################

    path('offlineGames', views.get_offline_games, name='offlineGames'),
    path('offlineGames/<str:offline_games_genre>',
         views.get_offline_games_by_genre, name='offlineGamesByGenre'),
]
