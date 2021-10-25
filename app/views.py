from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterUserForm

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