from django import forms
from app.models import User
from app.models import Packages
from app.models import Bookings


class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields="__all__" 

class PackagesForm(forms.ModelForm):
	class Meta:
		model=Packages
		fields="__all__" 
		

class BookingsForm(forms.ModelForm):
	class Meta:
		model=Bookings
		fields="__all__" 
				
