from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from users import serializers
from users.forms import CustomUserCreationForm
from users.models import CustomUser
from users.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from api.my_serializers import OnlineGameSerializer, OfflineGameSerializer, FilmSerializer, SeriesSerializer
import logging

logger = logging.getLogger(__name__)


def loginView(request):  # пользователь логинится
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            logger.info('the user '+email+' loginned')
            return redirect('home')
        else:
            messages.info(request, "Email or password is incorrect")
            logger.error('something went wrong in login view')
    context = {}
    return render(request, 'login.html', context)


def logoutView(request):  # пользователь логаутится
    logout(request)
    return redirect('login')


def registration(request):  # регистрация нового пользователя
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, 'аккаунт был создан для '+email)
            logger.info('user'+email+' was registrated')
    return render(request, 'registration.html', context={"form": form})


@login_required(login_url='login')  # получаем данные пользователя
@api_view(['GET'])
def getUser(request):
    user = CustomUser.objects.filter(email=request.user.email)
    serializer = UserSerializer(user, many=True)
    logger.warning('getting user')
    return Response(serializer.data)


@login_required(login_url='login')  # получаем фильмы из корзины пользователя
@api_view(['GET'])
def getUserFilms(request):
    films_basket = CustomUser.objects.get(
        email=request.user.email).films_basket.all()
    serializer = FilmSerializer(films_basket, many=True)
    logger.warning('getting user films')
    return Response(serializer.data)


@login_required(login_url='login')  # получаем сериалы из корзины пользователя
@api_view(['GET'])
def getUserSeries(request):
    series_basket = CustomUser.objects.get(
        email=request.user.email).series_basket.all()
    serializer = SeriesSerializer(series_basket, many=True)
    logger.warning('getting user series')
    return Response(serializer.data)


# получаем онлайн игры из корзины пользователя
@login_required(login_url='login')
@api_view(['GET'])
def getUserOnlineGames(request):
    online_games_basket = CustomUser.objects.get(
        email=request.user.email).online_games_basket.all()
    serializer = OnlineGameSerializer(online_games_basket, many=True)
    logger.warning('getting user online games')
    return Response(serializer.data)


# получаем офлайн игры из корзины пользователя
@login_required(login_url='login')
@api_view(['GET'])
def getUserOfflineGames(request):
    offline_games_basket = CustomUser.objects.get(
        email=request.user.email).offline_games_basket.all()
    serializer = OfflineGameSerializer(offline_games_basket, many=True)
    logger.warning('getting user offline games')
    return Response(serializer.data)


@login_required(login_url='login')
@api_view(['GET'])
def BuyOnlineGame(request, online_game_name):
    online_game = request.user.online_games_basket.get(name=online_game_name)
    online_game.bought = True
    online_game.save(update_fields=["bought"])
    serializer = OnlineGameSerializer(online_game)
    logger.warning('buying user online game')
    return Response(serializer.data)


@login_required(login_url='login')
@api_view(['GET'])
def BuyOfflineGame(request, offline_game_name):
    offline_game = request.user.offline_games_basket.get(
        name=offline_game_name)
    offline_game.bought = True
    offline_game.save(update_fields=["bought"])
    serializer = OfflineGameSerializer(offline_game)
    logger.warning('buying user offline game')
    return Response(serializer.data)


@login_required(login_url='login')
@api_view(['GET'])
def BuyFilm(request, film_name):
    film = request.user.films_basket.get(
        name=film_name)
    film.bought = True
    film.save(update_fields=["bought"])
    serializer = FilmSerializer(film)
    logger.warning('buying user film')
    return Response(serializer.data)


@login_required(login_url='login')
@api_view(['GET'])
def BuySeries(request, series_name):
    series = request.user.series_basket.get(
        name=series_name)
    series.bought = True
    series.save(update_fields=["bought"])
    serializer = SeriesSerializer(series)
    logger.warning('buying user series')
    return Response(serializer.data)
