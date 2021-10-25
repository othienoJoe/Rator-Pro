from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
	image = CloudinaryField('image')
	description = models.TextField()
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	email = models.EmailField()

	def __str__(self):
		return self.user.username
	@receiver(post_save, sender = User)
	def create_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user = instance)

	@receiver(post_save, sender = User)
	def save_profile(sender, instance, **kwargs):
		instance.profile.save()