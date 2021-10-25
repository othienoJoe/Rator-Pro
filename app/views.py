from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterUserForm, Profile

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
	return render(request, 'user/register.html', context)

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