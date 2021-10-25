from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# User registration form 
class RegisterUserForm(UserCreationForm):
	email = forms.EmailField()
	description = forms.CharField()

	class Meta:
		model = User
		fields = ['username', 'email', 'description', 'password1', 'password2']

# Profile and User update
class ProfileUpdateForm(forms.ModelForm):
  class Meta:
			model = Profile
			fields = ['image', 'description']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email']