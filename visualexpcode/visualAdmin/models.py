from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VisualUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	birth_date = models.DateField(),
	telephone = models.CharField(max_length=12)

	def __str__(self):
		return self.user.first_name + self.user.last_name

class Artist(models.Model):
	artist_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	stage_name = models.CharField(max_length=128)
	birth_date = models.DateField()

	def __str__(self):
		return self.stage_name

"""Abstract Model for the artworks"""
class Artwork(models.Model):
	artwork_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255) #Max supported by MySql text field
	description = models.CharField(max_length=255)
	publication_date = models.DateField()
	artists = models.ManyToManyField(Artist)
	#TODO Dimensions, coordinates ?

	def __str__(self):
		return self.title

	class Meta:
		abstract: True


class VideoArtwork(Artwork):
	length = models.IntegerField("Length (in seconds) :")
	file = models.FileField(upload_to='video/')

class ImageArtwork(Artwork):
	file = models.FileField(upload_to='image/')

class SoundArtwork(Artwork):
	length = models.IntegerField("Length (in seconds) : ")
	file = models.FileField(upload_to='video/')

