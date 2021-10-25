from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
	re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
	path('', views.index, name='home-view'),
	path('details/<int:id>/',views.project_details,name='details'),
	path('post/',views.post_project,name='post_project'),
	path('api/projects/', views.ProjectsList.as_view()),
	path('api/project/project-id/<int:pk>/',views.ProjectDescription.as_view()),
	path('rate/<int:pk>/',views.rate_project,name='rate'),
]