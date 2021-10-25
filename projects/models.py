from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from django.dispatch import receiver

# Create your models here.
class Rating(models.Model):
	source = models.CharField(max_length=50)
	rating = models.CharField(max_length=10)
	
	def __str__(self):
		return self.source

class Projects(models.Model):
	image = CloudinaryField('image')
	title = models.CharField(max_length=125)
	description = models.TextField() 
	link = models.CharField(max_length=600)
	ratings = GenericRelation(Rating, related_query_name='projects')
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date_posted']

class ProjectsApi(models.Model):
	title = models.CharField(max_length=40)
	description = models.TextField()

Rate_Choices = [
	(1, '1 - Trash'),
	(2, '2 - Terrible'),
	(3, '3 - Bad'),
	(4, '4 - OK'),
	(5, '5 - Good'),
	(6,'6 - Excellent'), 
]

class Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	project = models.ForeignKey(Projects, on_delete = models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	rate = models.PositiveSmallIntegerField(choices=Rate_Choices)