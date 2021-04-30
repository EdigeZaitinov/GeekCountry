from django.urls import path
from users import views

urlpatterns = [
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('registration', views.registration, name='registration'),
    path('users', views.getUsers, name='users'),
]
