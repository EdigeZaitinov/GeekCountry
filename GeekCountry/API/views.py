from django.shortcuts import render, redirect
from rest_framework import views
from API.models import Movie_genre, Film, Series, Game_genre, Online_game, Offline_game
from datetime import datetime
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from API.my_serializers import FilmSerializer, SeriesSerializer, OnlineGameSerializer, OfflineGameSerializer
from API.my_serializers import MovieGenreSerializer, GameGenreSerializer
from django.views import View


@login_required(login_url='Auth/login')
def home(request):
    date = datetime.now().date()
    return render(request, 'home.html', context={"today": date})


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_movie_genres(request):
    movie_genres = Movie_genre.objects.all()
    serializer = MovieGenreSerializer(movie_genres, many=True)
    return Response(serializer.data)


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_game_genres(request):
    game_genres = Game_genre.objects.all()
    serializer = GameGenreSerializer(game_genres, many=True)
    return Response(serializer.data)

######################### FILMS #################################


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_films(request):
    films = Film.films_manager.get_films()
    serializer = FilmSerializer(films, many=True)
    return Response(serializer.data)


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_films_by_genre(request, films_genre):
    films = Film.films_manager.get_films_by_genre(films_genre)
    serializer = FilmSerializer(films, many=True)
    return Response(serializer.data)


######################### SERIES ################################

@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_series(request):
    series = Series.series_manager.get_series()
    serializer = SeriesSerializer(series, many=True)
    return Response(serializer.data)


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_series_by_genre(request, series_genre):
    series = Series.series_manager.get_series_by_genre(series_genre)
    serializer = SeriesSerializer(series, many=True)
    return Response(serializer.data)

 ######################### ONLINE_GAMES ##########################


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_online_games(request):
    online_games = Online_game.online_game_manager.get_online_games()
    serializer = OnlineGameSerializer(online_games, many=True)
    return Response(serializer.data)


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_online_games_by_genre(request, online_games_genre):
    online_games = Online_game.online_game_manager.get_online_games_by_genre(
        online_games_genre)
    serializer = OnlineGameSerializer(online_games, many=True)
    return Response(serializer.data)

######################### OFFLINE_GAMES ##########################


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_offline_games(request):
    offline_games = Offline_game.offline_game_manager.get_offline_games()
    serializer = OfflineGameSerializer(offline_games, many=True)
    return Response(serializer.data)


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_offline_games_by_genre(request, offline_games_genre):
    offline_games = Offline_game.offline_game_manager.get_offline_games_by_genre(
        offline_games_genre)
    serializer = OfflineGameSerializer(offline_games, many=True)
    return Response(serializer.data)
