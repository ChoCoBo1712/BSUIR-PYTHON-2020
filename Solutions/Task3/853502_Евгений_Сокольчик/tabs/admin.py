from django.contrib import admin
from .models import Guitar, Guitarist, Genre, GuitaristPictures, GuitarPictures, Song, Manufacturer


admin.site.register(Guitar)
admin.site.register(GuitarPictures)
admin.site.register(Guitarist)
admin.site.register(GuitaristPictures)
admin.site.register(Manufacturer)
admin.site.register(Genre)
admin.site.register(Song)