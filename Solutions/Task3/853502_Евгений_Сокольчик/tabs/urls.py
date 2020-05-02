from django.urls import path

from .import views


urlpatterns = [
    path('', views.GuitarListView.as_view()),
    path('guitar/<slug:slug>/', views.GuitarDetailView.as_view(), name='guitar_detail'),
    path('guitarist/<slug:slug>/', views.GuitaristDetailView.as_view(), name='guitarist_detail'),
    path('manufacturer/<slug:slug>/', views.ManufacturerDetailView.as_view(), name='manufacturer_detail'),
    path('genre/<slug:slug>/', views.GenreDetailView.as_view(), name='genre_detail'),
    path('song/<slug:slug>/', views.SongDetailView.as_view(), name='song_detail'),
    path('songs/', views.SongListView.as_view(), name='songs')
]