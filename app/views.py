from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,authenticate
from app.models import Album,Song,Person
from app.forms import AlbumForm,signupform,signinform,Personform




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
			#sign_up(request,user)
			print(user.email)
			return redirect('sign_in')

	else:
		form = signupform()
	return render (request, 'sign_up.html',{'form':form})




def sign_in(request):
	if request.method =="POST":
		form = signinform(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			#login(request,user)
			print("so far so good")
			print(request.user.is_authenticated)
			print(username)
			print(password)
			return redirect('home')
	else:
		form = signinform()
	return render (request, 'sign_in.html',{'form':form})




def newperson(request):
	if request.method =="POST":
		form = Personform(request.POST or None)
		if form.is_valid():
			form.save()
		return redirect("people")

	else:
	   form = Personform()
	return render (request, 'newperson.html',{'form':form})


def people(request):
	people = Person.objects.all()
	return render (request, 'people.html', {'people':people})
