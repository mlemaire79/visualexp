from django.db import models
from django.contrib.auth.models import User
from itertools import chain
from polymorphic.models import PolymorphicModel

# Create your models here.
#ATTENTION: Le class order peut interferer avec le makemigrations

class VisualUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(),
    telephone = models.CharField(max_length=12)

    def __str__(self):
        return self.user.first_name + self.user.last_name

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


"""Abstract Model for the artworks"""
class Artwork(PolymorphicModel):
    artwork_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255) #Max supported by MySql text field
    description = models.CharField(max_length=255, blank=True)
    publication_date = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    #@TODO Dimensions, coordinates ?

    def __str__(self):
        return self.title


    def getType(self):
        """Return the type of Artwork.

        Return Values : 
        - "other"
        - "video"
        - "sound"
        - "image"
        """
        try: 
            self.soundartwork.title
        except SoundArtwork.DoesNotExist:
            try:
                self.videoartwork.title
            except VideoArtwork.DoesNotExist:
                try:
                    self.imageartwork.title
                except ImageArtwork.DoesNotExist:
                    return "other"
                else:
                    return "image"
            else:
                return "video"
        else:
            return "sound"



class VideoArtwork(Artwork):
    #artwork = models.ForeignKey()
    length = models.IntegerField("Length (in seconds) :", blank=True)
    file = models.FileField(upload_to='video/')

class ImageArtwork(Artwork):
    file = models.FileField(upload_to='image/')

class SoundArtwork(Artwork):
    length = models.IntegerField("Length (in seconds) : ", blank=True)
    file = models.FileField(upload_to='audio/')

class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    stage_name = models.CharField(max_length=128, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    artworks = models.ManyToManyField(Artwork)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.stage_name


class Exposition(models.Model):
    expo_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    author = models.CharField(max_length=64, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    artworks = models.ManyToManyField(Artwork, through='Display')

    def __str__(self):
        return self.title

class Display(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    exposition = models.ForeignKey(Exposition, on_delete=models.CASCADE)
    #@TODO add location of the artwork
    nbViews = models.IntegerField(default=0)
    deliveryTime = models.TimeField(blank=True,null=True)
    hasArrived = models.BooleanField(default=False)

    def __str__(self):
        return ""

    def addView(self):
        self.nbViews = self.nbViews + 1
        self.save
