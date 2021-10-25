from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from users.views import register_user

urlpatterns = [
	path('register/', register_user, name='register'),
	path('profile/', views.profile_view, name='profile'),
]