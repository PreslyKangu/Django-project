from django.urls import path
from django.contrib import admin

from app import views

urlpatterns = [
    path('albums/',            views.albums,       name='albums'),
    path('songs/',             views.songs,        name='songs'),
    path('newalbum/',          views.newalbum,     name='newalbum'),
    path('addsong/',           views.addsong,      name='addsong'),
     path('add/',           views.addalbum,      name='addalbum'),
    path('newsong/',           views.newsong,      name='newsong'),
    path('albumflani/<int:pk>/',views.albumflani,   name= 'albumflani'),
    #path('albumflani/<int:pk>/',views.albumflanisongs,   name= 'albumflanisongs')
]