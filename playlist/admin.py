from django.contrib import admin
from .models import Song, Playlist
from .forms import SongForm, PlaylistForm

admin.site.register(Playlist)
#admin.site.register(SongForm, PlaylistForm)
admin.site.register(Song)
# Register your models here.
