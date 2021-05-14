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


def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Email or password is incorrect")
    context = {}
    return render(request, 'login.html', context)


def logoutView(request):
    logout(request)
    return redirect('login')


def registration(request):
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, 'аккаунт был создан для '+email)
    return render(request, 'registration.html', context={"form": form})


@login_required(login_url='login')
@api_view(['GET'])
def getUser(request):
    user = CustomUser.objects.filter(email=request.user.email)
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@login_required(login_url='login')
@api_view(['GET'])
def getUserFilms(request):
    films_basket = CustomUser.objects.get(
        email=request.user.email).films_basket.all()
    serializer = FilmSerializer(films_basket, many=True)
    return Response(serializer.data)


@login_required(login_url='login')
@api_view(['GET'])
def getUserSeries(request):
    series_basket = CustomUser.objects.get(
        email=request.user.email).series_basket.all()
    serializer = FilmSerializer(series_basket, many=True)
    return Response(serializer.data)


@login_required(login_url='login')
@api_view(['GET'])
def getUserOnlineGames(request):
    online_games_basket = CustomUser.objects.get(
        email=request.user.email).online_games_basket.all()
    serializer = OnlineGameSerializer(online_games_basket, many=True)
    return Response(serializer.data)


@login_required(login_url='login')
@api_view(['GET'])
def getUserOfflineGames(request):
    offline_games_basket = CustomUser.objects.get(
        email=request.user.email).offline_games_basket.all()
    serializer = OfflineGameSerializer(offline_games_basket, many=True)
    return Response(serializer.data)
