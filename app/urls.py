from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('register/', register_user, name='register'),
	path('login/', LoginView.as_view(template_name = 'login.html'), name = 'login'),
	path('accounts/profile/', views.profile_view, name='profile'),
	path('logout/', LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
	path('update/', views.update, name='update'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)