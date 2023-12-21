from django.urls import path
from . import views
from .views import SignUpView
urlpatterns = [
    path('', views.home, name='home'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('request/', views.request_song, name='request_song'),
    path('search/', views.search_songs, name='search_songs'),
]

'''
    path('request/', views.request_song, name='request_song'),
    path('playlists/create/', views.create_playlist, name='create_playlist'),
    path('playlists/<int:pk>/detail/', views.playlist_detail, name='playlist_detail'),
    path('playlists/<int:pk>/add_track/', views.add_track_to_playlist, name='add_track_to_playlist'),
    path('playlists/<int:pk>/delete/', views.delete_playlist, name='delete_playlist'),
    path('playlists/', views.playlist_list, name='playlist_list'),
    '''