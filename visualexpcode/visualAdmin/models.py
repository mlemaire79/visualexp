from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class visualUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	birth_date = models.DateField(),
	telephone = models.CharField(max_length=12)

	def __str__(self):
		return self.user.first_name + self.user.last_name

class artist(models.Model):
	artist_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	stage_name = models.CharField(max_length=128)
	birth_date = models.DateField()

	def __str__(self):
		return self.stage_name

