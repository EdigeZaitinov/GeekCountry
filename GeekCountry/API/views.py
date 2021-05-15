from django.shortcuts import render, redirect
from api.models import Movie_genre, Film, Series, Game_genre, Online_game, Offline_game
from datetime import datetime
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.my_serializers import FilmSerializer, SeriesSerializer, OnlineGameSerializer, OfflineGameSerializer
from api.my_serializers import MovieGenreSerializer, GameGenreSerializer
from api.forms import OnlineGameCollectForm, OfflineGameCollectForm, SeriesCollectForm, FilmCollectForm
from users.models import CustomUser
import logging

logger = logging.getLogger(__name__)

# пользователь дома


@login_required(login_url='Auth/login')
def home(request):
    date = datetime.now().date()
    logger.warning('user '+request.user.email+' at home')
    return render(request, 'home.html', context={"today": date})

# пользователь получает жанры фильмов


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_movie_genres(request):
    movie_genres = Movie_genre.objects.all()
    serializer = MovieGenreSerializer(movie_genres, many=True)
    logger.warning('user '+request.user.email+' getting movie genres')
    return Response(serializer.data)

# пользователь получает жанры игр


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_game_genres(request):
    game_genres = Game_genre.objects.all()
    serializer = GameGenreSerializer(game_genres, many=True)
    logger.warning('user '+request.user.email+' getting game genres')
    return Response(serializer.data)

######################### FILMS #################################

# пользователь получает все фильмы


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_films(request):
    films = Film.films_manager.get_films()
    serializer = FilmSerializer(films, many=True)
    logger.warning('user '+request.user.email+' got all films')
    return Response(serializer.data)


# пользователь получает все фильмы одного жанра
@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_films_by_genre(request, films_genre):
    films = Film.films_manager.get_films_by_genre(films_genre)
    serializer = FilmSerializer(films, many=True)
    logger.warning('user '+request.user.email+' got all films by genre')
    return Response(serializer.data)


# пользователь получает фильм по названию
@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_film(request, film_name):
    films = Film.films_manager.filter(name=film_name)[:1]
    serializer = FilmSerializer(films, many=True)
    logger.warning('user '+request.user.email+' got films by name')
    return Response(serializer.data)

# пользователь заносит фильм в корзину


@login_required(login_url='Auth/login')
def collect_film(request, film_name):
    if request.method == 'POST':
        film_form = FilmCollectForm(request.POST)
        if film_form.is_valid():
            user = CustomUser.objects.filter(email=request.user.email)[:1]
            film = Film.films_manager.get(name=film_name)
            user[0].films_basket.add(film)
            logger.warning('user '+request.user.email +
                           ' added '+film.name+' to films basket')
    return render(request, 'forms/film_collect.html', context={'film_form': film_form})

######################### SERIES ################################

# пользователь получает все сериалы


@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_series(request):
    series = Series.series_manager.get_series()
    serializer = SeriesSerializer(series, many=True)
    logger.warning('user '+request.user.email+' got all series')
    return Response(serializer.data)


# пользователь получает все сериалы одного жанра
@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_series_by_genre(request, series_genre):
    series = Series.series_manager.get_series_by_genre(series_genre)
    serializer = SeriesSerializer(series, many=True)
    logger.warning('user '+request.user.email+' got all series by genre')
    return Response(serializer.data)


# пользователь получает сериал по названию
@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_one_series(request, series_name):
    series = Series.series_manager.filter(name=series_name)[:1]
    serializer = SeriesSerializer(series, many=True)
    logger.warning('user '+request.user.email+' got series by name')
    return Response(serializer.data)


# пользователь заносит сериал в корзину
@login_required(login_url='Auth/login')
def collect_series(request, series_name):
    if request.method == 'POST':
        series_form = SeriesCollectForm(request.POST)
        if series_form.is_valid():
            user = CustomUser.objects.filter(email=request.user.email)[:1]
            series = Series.series_manager.get(name=series_name)
            user[0].series_basket.add(series)
            logger.warning('user '+request.user.email+' added ' +
                           series.name+' to series basket')
    return render(request, 'forms/series_collect.html', context={'series_form': series_form})

 ######################### ONLINE_GAMES ##########################


# пользователь получает все онлайн игры
@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_online_games(request):
    online_games = Online_game.online_game_manager.get_online_games()
    serializer = OnlineGameSerializer(online_games, many=True)
    logger.warning('user '+request.user.email+' got all online games')
    return Response(serializer.data)


# пользователь получает все онлайн игры одного жанра
@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_online_games_by_genre(request, online_games_genre):
    online_games = Online_game.online_game_manager.get_online_games_by_genre(
        online_games_genre)
    serializer = OnlineGameSerializer(online_games, many=True)
    logger.warning('user '+request.user.email+' got all online games by genre')
    return Response(serializer.data)


# пользователь получает онлайн игру по названию
@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_online_game(request, online_game_name):
    online_game = Online_game.online_game_manager.filter(name=online_game_name)[
        :1]
    serializer = OnlineGameSerializer(online_game, many=True)
    logger.warning('user '+request.user.email+' got online game by name')
    return Response(serializer.data)


# пользователь заносит онлайн игру в корзину
@login_required(login_url='Auth/login')
def collect_online_game(request, online_game_name):
    if request.method == 'POST':
        online_game_form = OnlineGameCollectForm(request.POST)
        if online_game_form.is_valid():
            user = CustomUser.objects.filter(email=request.user.email)[:1]
            online_game = Online_game.online_game_manager.get(
                name=online_game_name)
            user[0].online_games_basket.add(online_game)
            logger.warning('user '+request.user.email+' added '+online_game.name +
                           ' to online game basket')
    return render(request, 'forms/online_game_collect.html', context={'online_game_form': online_game_form})

######################### OFFLINE_GAMES ##########################


# пользователь получает все офлайн игры
@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_offline_games(request):
    offline_games = Offline_game.offline_game_manager.get_offline_games()
    serializer = OfflineGameSerializer(offline_games, many=True)
    logger.warning('user '+request.user.email+' got all offline games')
    return Response(serializer.data)


# пользователь получает все офлайн игры одного жанра
@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_offline_games_by_genre(request, offline_games_genre):
    offline_games = Offline_game.offline_game_manager.get_offline_games_by_genre(
        offline_games_genre)
    serializer = OfflineGameSerializer(offline_games, many=True)
    logger.warning('user '+request.user.email +
                   ' got all offline games by genre')
    return Response(serializer.data)


# пользователь получает офлайн игру по названию
@login_required(login_url='Auth/login')
@api_view(['GET'])
def get_offline_game(request, offline_game_name):
    offline_game = Offline_game.offline_game_manager.filter(
        name=offline_game_name)[:1]
    serializer = OfflineGameSerializer(offline_game, many=True)
    logger.warning('user '+request.user.email+' got offline game by name')
    return Response(serializer.data)


# пользователь заносит офлайн игру в корзину
@login_required(login_url='Auth/login')
def collect_offline_game(request, offline_game_name):
    if request.method == 'POST':
        offline_game_form = OfflineGameCollectForm(request.POST)
        if offline_game_form.is_valid():
            user = CustomUser.objects.filter(email=request.user.email)[:1]
            offline_game = Offline_game.offline_game_manager.get(
                name=offline_game_name)
            user[0].offline_games_basket.add(offline_game)
            logger.warning('user'+request.user.email+' added ' +
                           offline_game.name+' to offline game basket')
    return render(request, 'forms/offline_game_collect.html', context={'offline_game_form': offline_game_form})
