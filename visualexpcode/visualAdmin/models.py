from django.db import models
from django.contrib.auth.models import User
from itertools import chain

# Create your models here.

class VisualUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	birth_date = models.DateField(),
	telephone = models.CharField(max_length=12)

	def __str__(self):
		return self.user.first_name + self.user.last_name

#ATTENTION: Le class order peut interférer avec le makemigrations
class Tag(models.Model):
	tag_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.name

	def get_artworks(self):
		return list(chain(self.videoartwork_set.all(),self.imageartwork_set.all(),self.soundartwork_set.all()))

	def get_artists(self):
		return list(chain(self.artist_set.all()))

class Artist(models.Model):
	artist_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	stage_name = models.CharField(max_length=128, blank=True)
	birth_date = models.DateField(blank=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.stage_name

	def get_artworks(self):
		"""We have 3 different QuerySets that need to be merged into a single list """
		return list(chain(self.videoartwork_set.all(),self.imageartwork_set.all(),self.soundartwork_set.all()))


"""Abstract Model for the artworks"""
class Artwork(models.Model):
	artwork_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255) #Max supported by MySql text field
	description = models.CharField(max_length=255, blank=True)
	publication_date = models.DateField(blank=True, null=True)
	artists = models.ManyToManyField(Artist)
	tags = models.ManyToManyField(Tag)
	#TODO Dimensions, coordinates ?

	def __str__(self):
		return self.title

	class Meta:
		abstract = True


class VideoArtwork(Artwork):
	length = models.IntegerField("Length (in seconds) :", blank=True)
	file = models.FileField(upload_to='video/')

class ImageArtwork(Artwork):
	file = models.FileField(upload_to='image/')

class SoundArtwork(Artwork):
	length = models.IntegerField("Length (in seconds) : ", blank=True)
	file = models.FileField(upload_to='audio/')


