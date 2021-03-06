from django.urls import path
from django.contrib import admin
from app import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',                views.home,              name='home'),
    path('about/',               views.about,             name='about'),
    path('albums/',              views.albums,            name='albums'),
    path('songs/',               views.songs,             name='songs'),
    path('newalbum/',            views.newalbum,          name='newalbum'),
    path('addsong/',             views.addsong,           name='addsong'),
    path('add/',                 views.addalbum,          name='addalbum'),
    path('newsong/',             views.newsong,           name='newsong'),
    path('sign_up/',             views.sign_up,           name='sign_up'),
    path('sign_in/',             views.sign_in,           name='sign_in'),
    path('people/',              views.people,            name='people'),
    path('newperson/',           views.newperson,         name='newperson'),
    path('ultra_album_model/',   views.ultra_album_model, name='ultra_album_model'), 
    path('albumflani/<int:pk>/', views.albumflani,        name='albumflani'),
    #path('albumflani/<int:pk>/',views.albumflanisongs,   name= 'albumflanisongs')
]