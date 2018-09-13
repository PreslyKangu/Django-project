from django.shortcuts import render,redirect,HttpResponseRedirect
from app.models import Album,Song
from app.forms import AlbumForm
from app.forms import signupform

# Create your views here.
def home(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')

def albums(request):
	albums = Album.objects.all()
	return render(request,'albums.html',{ 'albums':albums})

def songs(request):
	songs = Song.objects.all()
	return render(request,'songs.html',{ 'songs':songs})



#ndio hii io io view
def newalbum(request):
	return render(request,'addalbum.html')



def addalbum(request):
	a = request.GET['artist']
	b = request.GET['album_title']
	c = request.GET['genre']
	d = request.GET['album_logo']
	album = Album.objects.create(
		artist =a,
		genre = c,
		album_logo = d,
		album_title = b
		)
	album.save()
	return redirect('albums')

def newsong(request,pk):
	return render(request,'newsong.html')


def addsong(request,pk):
	album = get_object_or_404(Album,pk=pk)
	song_type = request.GET['song_type']
	song_title = request.GET['song_title']
	song = Song.objects.create(
		album = album,
		song_type = song_type,
		song_title = song_title
		)
	song.save()
	redirect('albumflani',pk=pk)
	return render(request,'newsong.html')

def albumflani(request,pk):
	#album = get_object_or_404(Album,pk=pk)
	#producer = get_object_or_404(Producer,pk=pk)
	#actors = Actor.objects.select_related().filter(programme = programme_id)
	album = Album.objects.get(id=pk)
	songs = Song.objects.select_related().filter(album_id=pk)
	return render(request,'albumflani.html',{'album':album,'songs':songs})



def ultra_album_model(request):
	if request.method == "POST":
		form = AlbumForm(request.POST or None)
		if form.is_valid():
			form.save()
			print("added")
			return redirect('albums')

	else:
		form = AlbumForm()
	return render (request, 'ultra_album_model.html',{'form':form})



def sign_up(request):
	if request.method == "POST":
		form = signupform(request.POST or None)
		if form.is_valid():
			user = form.save()
			#Login(request,user)
			print(user.email)
			return redirect('home')

	else:
		form = signupform()
	return render (request, 'sign_up.html',{'form':form})