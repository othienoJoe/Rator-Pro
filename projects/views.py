from django.shortcuts import render,get_object_or_404, redirect
from .models import Projects, Review
from .forms import PostProjectsForm, RateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  ProjectsApi
from .serializer import ApiSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
def index(request):
	projects = Projects.objects.all()
	query = request.GET.get('q')
	if query:
		projects = projects.filter(title__icontains=query)

	context = {
		'projects': projects,
	}
	return render(request,'index.html',context)

def project_details(request,id):
  project = get_object_or_404(Projects,id=id)
    
  context = {
    'project':project,
  }
  return render(request,'details.html',context)

def projects_reviews(request,id):
	reviews = get_object_or_404(Review,id=id)
	context = {
		'reviews':reviews,
	}
	return render(request,'details.html',context)

@login_required
def rate_project(request, pk):
	project = Projects.objects.get(pk=pk)
	user = request.user

	if request.method == 'POST':
		form = RateForm(request.POST)
		if form.is_valid():
			rate = form.save(commit=False)
			rate.user = user
			rate.project = project
			rate.save()
			return redirect('home-view')
	else:
		form = RateForm()

	context = {
		'form': form, 
		'project': project,
	}
	return render(request,'rate.html',context)

@login_required
def post_project(request):
	if request.method == 'POST':
		print(request.POST)
		form = PostProjectsForm(request.POST,request.FILES)
		if form.is_valid():
			addProject = form.save(commit=False)
			addProject.save()
			
			messages.success(request,'Your project has been posted successfully')
			return redirect('home-view')
	else:
		form = PostProjectsForm()

	context = {'form':form,}
	return render(request,'all_projects.html',context)

class ProjectsList(APIView):
  def get(self, request, format=None):
			all_projects = ProjectsApi.objects.all()
			serializers = ApiSerializer(all_projects, many=True)
			return Response(serializers.data)

  def post(self, request, format=None):
			serializers = ApiSerializer(data=request.data)
			if serializers.is_valid():
				serializers.save()
				return Response(serializers.data, status=status.HTTP_201_CREATED)
			return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  permission_classes = (IsAdminOrReadOnly,)

class ProjectDescription(APIView):
	permission_classes = (IsAdminOrReadOnly,)
	def get_project(self, pk):
		try:
			return ProjectsApi.objects.get(pk=pk)
		except ProjectsApi.DoesNotExist:
			raise 404

	def get(self, request, pk, format=None):
		project = self.get_merch(pk)
		serializers = ApiSerializer()
		return Response(serializers.data)

	def put(self, request, pk, format=None):
		project = self.get_project(pk)
		serializers = ApiSerializer(project, request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data)
		else:
			return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# Make a delete option here
	def delete(self, request, pk, format=None):
		project = self.get_project(pk)
		project.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
