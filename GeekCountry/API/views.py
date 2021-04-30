from django.shortcuts import render, redirect
from API.models import Movie_genre, Film, Series, Game_genre, Online_game, Offline_game
from datetime import datetime
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from API.my_serializers import FilmSerializer, SeriesSerializer, OnlineGameSerializer, OfflineGameSerializer
from API.my_serializers import MovieGenreSerializer, GameGenreSerializer


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
def get_films(request):
    films = Film.films_manager.all()
    serializer = FilmSerializer(films, many=True)
    return Response(serializer.data)


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_series(request):
    series = Series.series_manager.all()
    serializer = SeriesSerializer(series, many=True)
    return Response(serializer.data)


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_game_genres(request):
    game_genres = Game_genre.objects.all()
    serializer = GameGenreSerializer(game_genres, many=True)
    return Response(serializer.data)


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_online_games(request):
    online_games = Online_game.online_game_manager.all()
    serializer = OnlineGameSerializer(online_games, many=True)
    return Response(serializer.data)


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_offline_games(request):
    offline_games = Offline_game.offline_game_manager.all()
    serializer = OfflineGameSerializer(offline_games, many=True)
    return Response(serializer.data)
