from django import forms
from app.models import Album
from django.contrib.auth.models import User

class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ('album_logo','artist','album_title','genre')	


class signupform(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email','username','password')
	
		
		
