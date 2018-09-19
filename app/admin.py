from django.contrib import admin
from app.models import Album, Song,Person
# Register your models here.

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Person)