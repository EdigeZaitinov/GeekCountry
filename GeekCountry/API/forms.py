from django.forms import ModelForm
from api.models import Online_game, Offline_game, Film, Series


class OnlineGameCollectForm(ModelForm):
    class Meta:
        model = Online_game
        fields = '__all__'


class OfflineGameCollectForm(ModelForm):
    class Meta:
        model = Offline_game
        fields = '__all__'


class FilmCollectForm(ModelForm):
    class Meta:
        model = Film
        fields = '__all__'


class SeriesCollectForm(ModelForm):
    class Meta:
        model = Series
        fields = '__all__'
