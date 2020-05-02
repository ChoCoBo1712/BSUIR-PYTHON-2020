from django.views.generic import ListView, DetailView

from .models import Guitar, Guitarist, Manufacturer, Genre, Song


class GuitarListView(ListView):
    model = Guitar
    queryset = Guitar.objects.all()
    template_name = 'tabs/guitars.html'

class SongListView(ListView):
    model = Song
    queryset = Song.objects.all()
    template_name = 'tabs/songs.html'

class GuitarDetailView(DetailView):
    model = Guitar
    slug_field = 'url'

class GuitaristDetailView(DetailView):
    model = Guitarist
    slug_field = 'url'

class ManufacturerDetailView(DetailView):
    model = Manufacturer
    slug_field = 'url'

class GenreDetailView(DetailView):
    model = Genre
    slug_field = 'url'

class SongDetailView(DetailView):
    model = Song
    slug_field = 'url'
