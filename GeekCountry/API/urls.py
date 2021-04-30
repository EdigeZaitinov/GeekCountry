from django.urls import path
from API import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movieGenres', views.get_movie_genres, name='movieGenres'),
    path('films', views.get_films, name='films'),
    path('series', views.get_series, name='series'),
    path('gameGenres', views.get_game_genres, name='gameGenres'),
    path('onlineGames', views.get_online_games, name='onlineGames'),
    path('offlineGames', views.get_offline_games, name='offlineGames'),
]
