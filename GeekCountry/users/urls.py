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
    path('user/onlineGames/<str:online_game_name>/buy',
         views.BuyOnlineGame, name='BuyOnlineGame'),
    path('user/offlineGames/<str:offline_game_name>/buy',
         views.BuyOfflineGame, name='BuyOfflineGame'),
    path('user/films/<str:film_name>/buy',
         views.BuyFilm, name='BuyFilm'),
    path('user/series/<str:series_name>/buy',
         views.BuySeries, name='BuySeries'),
]
