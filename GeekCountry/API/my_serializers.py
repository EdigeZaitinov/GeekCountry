from rest_framework import serializers
from api.models import Movie_genre, Film, Series, Online_game, Offline_game


class MovieGenreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'


class GameGenreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class OnlineGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Online_game
        fields = '__all__'


class OfflineGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offline_game
        fields = '__all__'
