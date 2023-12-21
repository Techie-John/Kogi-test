from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Playlist, Song
from .forms import PlaylistForm, SongForm

def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists/playlist_list.html', {'playlists': playlists})

def playlist_create(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playlist_list')
    else:
        form = PlaylistForm()
    return render(request, 'playlists/playlist_create.html', {'form': form})

def playlist_detail(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    songs = playlist.songs.all()
    return render(request, 'playlists/playlist_detail.html', {'playlist': playlist, 'songs': songs})

def playlist_edit(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    if request.method == 'POST':
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            form.save()
            return redirect('playlist_detail', pk=playlist.pk)
    else:
        form = PlaylistForm(instance=playlist)
    return render(request, 'playlists/playlist_edit.html', {'form': form})

def song_create(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, playlist=playlist)
        if form.is_valid():
            form.save()
            return redirect('playlist_detail', pk=playlist.pk)
    else:
        form = SongForm(playlist=playlist)
    return render(request, 'playlists/song_create.html', {'form': form})
# Create your views here.
