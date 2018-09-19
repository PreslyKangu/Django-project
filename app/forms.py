from django import forms
from app.models import Album,Person
from django.contrib.auth.models import User

class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ('album_logo','artist','album_title','genre')	


class signupform(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email','username','password')
	
		
		
class signinform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class Personform(forms.ModelForm):
	"""docstring for Person"""
	class Meta:
		model = Person
		fields = ('name','age','picture')
