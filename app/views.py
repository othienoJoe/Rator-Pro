from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterUserForm

# Create your views here.
def register_user(request):
	if request.method == 'POST':
		form = RegisterUserForm(request.POST, request.FILES)