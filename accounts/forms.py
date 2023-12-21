from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import RequestedSong, User
from django.forms import ModelForm
#from .models import Playlist, Track

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("email", "username", "password", "profile_photo", "bio",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields

'''
class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('name',)

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('title', 'artist', 'album', 'genre', 'duration')
'''
class RequestForm(ModelForm):
    class Meta:
        model = RequestedSong
        fields = ('SongName', 'artistName', 'year_released', 'trending_platforms')
