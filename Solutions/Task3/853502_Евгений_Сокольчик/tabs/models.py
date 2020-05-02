from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Guitarist(models.Model):
    name = models.CharField('Guitarist', max_length=100)
    age = models.PositiveSmallIntegerField('Age', default=18)
    description = models.TextField('Description')
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("guitarist_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Guitarist'
        verbose_name_plural = 'Guitarists'


class Manufacturer(models.Model):
    name = models.CharField('Manufacturer', max_length=100)
    description = models.TextField('Description')
    logo = models.ImageField('Logo', upload_to='manufacturer_logos/', default='manufacturer_logos/logo.png')
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("manufacturer_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'


class Genre(models.Model):
    name = models.CharField('Genre', max_length=100)
    description = models.TextField('Description')
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("genre_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Guitar(models.Model):
    name = models.CharField('Guitar', max_length=100)
    description = models.TextField('Description')
    guitarists = models.ManyToManyField(Guitarist, verbose_name='Guitarists')
    genres = models.ManyToManyField(Genre, verbose_name='Genres')
    manufacturers = models.ManyToManyField(Manufacturer, verbose_name='Manufacturers')
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("guitar_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Guitar'
        verbose_name_plural = 'Guitars'


class Song(models.Model):
    name = models.CharField('Song', max_length=100)
    author = models.CharField('Author', max_length=100, default='Author')
    lyrics = models.TextField('Lyrics')
    genres = models.ManyToManyField(Genre, verbose_name='Genres')
    song = EmbedVideoField('Song')
    tab = models.CharField('Tab', max_length=100, default='songsterr.com')
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("song_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'


class GuitarPictures(models.Model):
    name = models.CharField('Guitar Picture', max_length=100)
    image = models.ImageField('Image', upload_to='guitar_pictures/')
    guitar = models.ForeignKey(Guitar, verbose_name='Guitar', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Guitar Picture'
        verbose_name_plural = 'Guitar Pictures'


class GuitaristPictures(models.Model):
    name = models.CharField('Guitarist Picture', max_length=100)
    image = models.ImageField('Image', upload_to='guitarist_pictures/')
    guitar = models.ForeignKey(Guitarist, verbose_name='Guitarist', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Guitarist Picture'
        verbose_name_plural = 'Guitarist Pictures'
