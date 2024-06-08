from django.shortcuts import render
from albums.models import Album
from musicians.models import Musician


def home(request):
    music_data = Musician.objects.all()
    album_data = Album.objects.all()

    return render(request, 'home.html', {'music_data' : music_data, 'album_data' : album_data})