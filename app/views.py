from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterUserForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def register_user(request):
	if request.method == 'POST':
		form = RegisterUserForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Account Has Been Created Successfully')
			return redirect('login')

	else:
		form = RegisterUserForm()

	context = {
		'form': form
	}
	return render(request, 'register.html', context)

@login_required
def update(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your Account Has Been Updated Successfully!')
			return redirect('profile')

@login_required
def profile_view(request):
	profile = Profile.objects.get(user = request.user.id)
	return render(request, 'user/profile.html')

# Updating the forms
def update(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES,
		instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Successfully updated your account!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/update.html', context)