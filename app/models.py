from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
	image = CloudinaryField('image')
	description = models.TextField()
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	email = models.EmailField()