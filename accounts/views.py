from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import RequestedSong, Song, User, PromotedSong
from django.db.models import Q
#from .forms import PlaylistForm, TrackForm



def home(request):
    users = User.objects.all()
    promoted = PromotedSong.objects.all().order_by('-last_updated')
    allSongs = Song.objects.all().order_by('-last_updated')
    return render(request, "home.html", context={"allSongs" : allSongs, "users": users, "promoted": promoted})



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def search_songs(request): 
    template_path = 'search_result.html'

    search_query = request.GET.get('search', None)

    if search_query: 
        search_result = Song.objects.filter(
            Q(songName__icontains=search_query) | 
            Q(album__albumName__icontains=search_query) | 
            Q(album__artist__artistName__icontains=search_query)
        ).distinct()
    else: 
        search_result = Song.objects.all()
        
    context = {'search_result' : search_result, 'search_query' : search_query}
    return render(request, template_path, context)

@login_required
def request_song(request):
    form = RequestedSong
    return render(request, 'request_song.html', {'form': form})




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_detail', username=form.cleaned_data.get('username'))
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


'''
def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            return redirect('playlist_detail', pk=playlist.pk)
    else:
        form = PlaylistForm()
    return render(request, 'playlists/create.html', {'form': form})

def playlist_detail(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    tracks = playlist.tracks.all()
    return render(request, 'playlists/detail.html', {'playlist': playlist, 'tracks': tracks})

def add_track_to_playlist(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    track = Track.objects.get(pk=request.POST['track_id'])
    playlist.tracks.add(track)
    return redirect(playlist_detail, pk=playlist.pk)

def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists/list.html', {'playlists': playlists})

def delete_playlist(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    playlist.delete()
    return redirect(playlist_list)

# Create your views here.
'''