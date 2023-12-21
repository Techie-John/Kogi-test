from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Artist, RequestedSong, User, Album, Song, PromotedSong
from .forms import CustomUserCreationForm, CustomUserChangeForm 

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
    "email",
    "username",
    "password",
    "profile_photo",
    "bio",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("bio",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("bio","profile_photo",)}),)


admin.site.register(User, CustomUserAdmin)
admin.site.register(RequestedSong)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id", "artistName", "created", "last_updated")

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("id", "album", "song", "songName", "songThumbnail", "created", "last_updated" )

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("artist", "albumName", "created", "last_updated")

@admin.register(PromotedSong)
class PromotedAdmin(admin.ModelAdmin):
    list_display = ("id", "album", "song", "songName", "songThumbnail", "created", "last_updated" )
    
# Register your models here.