from django.urls import path
from . import views

urlpatterns = [
    path('playlists/', views.playlist_list, name='playlist_list'),
    path('playlists/create/', views.playlist_create, name='playlist_create'),
    path('playlists/<int:pk>/detail/', views.playlist_detail, name='playlist_detail'),
    path('playlists/<int:pk>/edit/', views.playlist_edit, name='playlist_edit'),
    path('playlists/<int:pk>/songs/create/', views.song_create, name='song_create'),
]