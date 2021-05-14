from django.urls import path
from users import views

urlpatterns = [
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('registration', views.registration, name='registration'),
    path('user', views.getUser, name='user'),
    path('user/onlineGames', views.getUserOnlineGames, name='userOnlineGames'),
    path('user/offlineGames', views.getUserOfflineGames, name='userOfflineGames'),
    path('user/films', views.getUserFilms, name='userFilms'),
    path('user/series', views.getUserSeries, name='userSeries'),
]
