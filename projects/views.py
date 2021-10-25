from django.shortcuts import render
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
