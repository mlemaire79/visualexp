from django.db import models
from django.contrib.auth.models import User
from itertools import chain
from polymorphic.models import PolymorphicModel
from parler.models import TranslatableModel, TranslatedFields
#from parler.managers import TranslatableManager
from .managers import ArtworkManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.
#ATTENTION: Le class order peut interferer avec le makemigrations
# @TODO Ajouter les commentaires pour les traducteurs

class Tag(TranslatableModel):
    tag_id = models.AutoField(primary_key=True)

    translations = TranslatedFields (
    # Translators: Form label for Tag name Field
    name = models.CharField(max_length=30, verbose_name=_("Libellé du tag")),
    description = models.CharField(max_length=255, blank=True, verbose_name=_("Description du tag")),
    )

    def __str__(self):
        return self.name

    def get_artworks(self):
        return list(chain(self.videoartwork_set.all(),self.imageartwork_set.all(),self.soundartwork_set.all()))

    def get_artists(self):
        return list(chain(self.artist_set.all()))

        class Meta:
            # Translators: Model name for Tag(s)
            verbose_name = _('Etiquette')
            verbose_name_plural = _('Etiquettes')


"""Abstract Model for the artworks"""
class Artwork(PolymorphicModel, TranslatableModel):

    objects = ArtworkManager()

    artwork_id = models.AutoField(primary_key=True)

    translations = TranslatedFields (
        title = models.CharField(max_length=255, verbose_name=_("Titre de l'oeuvre")), #Max supported by MySql text field
        description = models.TextField(blank=True, verbose_name=_("Description de l'oeuvre")),
    )
    publication_date = models.DateField(blank=True, null=True, verbose_name=_("Date de publication"))
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

    class Meta:
        # Translators: Model name for Artwork
        verbose_name = _('Oeuvre')
        verbose_name_plural = _('Oeuvres')



class VideoArtwork(Artwork):
    #artwork = models.ForeignKey()
    length = models.IntegerField(_("Durée (En secondes)"), blank=True, null=True)
    file = models.FileField(upload_to='video/', verbose_name=_("Vidéo"))

    class Meta:
        # Translators: Model name for VideoArtwork(s)
        verbose_name = _('Oeuvre Vidéo')
        verbose_name_plural = _('Oeuvres Vidéo')

class ImageArtwork(Artwork):
    file = models.FileField(upload_to='image/', verbose_name=_("Image"))

    class Meta:
        # Translators: Model name for ImageArtwork(s)
        verbose_name = _('Oeuvre Image')
        verbose_name_plural = _('Oeuvres Image')

class SoundArtwork(Artwork):
    length = models.IntegerField(_("Durée (en secondes)"), blank=True, null=True)
    file = models.FileField(upload_to='audio/', verbose_name=_("Son"))

    class Meta:
        # Translators: Model name for SoundArtwork(s)
        verbose_name = _('Oeuvre Sonore')
        verbose_name_plural = _('Oeuvres Sonore')

class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64, verbose_name=_("Prénom"))
    last_name = models.CharField(max_length=64, verbose_name=_("Nom"))
    stage_name = models.CharField(max_length=128, blank=True, verbose_name=_("Pseudonyme"))
    birth_date = models.DateField(blank=True, null=True, verbose_name=_("Date de naissance"))
    artworks = models.ManyToManyField(Artwork)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.stage_name

    class Meta:
        # Translators: Model name for Artist(s)
        verbose_name = _('Artiste')
        verbose_name_plural = _('Artistes')

#@TODO Add opening/closing hours
class Exposition(TranslatableModel):
    expo_id = models.AutoField(primary_key=True)
    translations = TranslatedFields (
        title = models.CharField(max_length=64, verbose_name=_("Titre de l'exposition")),
        description = models.TextField(verbose_name=_("Description")),
    )
    author = models.CharField(max_length=64, blank=True, verbose_name=_("Auteur de l'exposition"))
    start_date = models.DateField(verbose_name=_("Début de l'exposition"))
    end_date = models.DateField(verbose_name=_("Fin de l'exposition"))
    artworks = models.ManyToManyField(Artwork, through='Display')


    def __str__(self):
        return self.title

    class Meta:
        # Translators: Model name for Exposition(s)
        verbose_name = _('Exposition')
        verbose_name_plural = _('Expositions')

class Display(TranslatableModel):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    exposition = models.ForeignKey(Exposition, on_delete=models.CASCADE)
    translations = TranslatedFields(
        description = models.TextField(_("Description")),
    )
    #@TODO add location of the artwork
    nbViews = models.IntegerField(default=0, verbose_name=_("Nombre de vues"))
    deliveryTime = models.TimeField(blank=True,null=True, verbose_name=_("Date de livraison"))
    hasArrived = models.BooleanField(default=False, verbose_name=_("Arrivée"))

    def __str__(self):
        return self.exposition.__str__() + " - " + self.artwork.__str__()

    def add_view(self):
        self.nbViews = self.nbViews + 1
        self.save

    class Meta:
        # Translators: Model name for Display(s)
        verbose_name = _('Exposé')
        verbose_name_plural = _('Exposés')


class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    exposition= models.ForeignKey(Exposition, on_delete=models.CASCADE)
    start_date=models.DateTimeField(verbose_name=_("Début de la tâche"))
    end_date=models.DateTimeField(verbose_name=_("Fin de la tâche"))
    name = models.CharField(max_length=64, verbose_name=_("Nom de la tâche"))
    description = models.TextField(blank=True, verbose_name=_("Description de la tâche"))

    def __str__ (self):
        return name

    def get_users(self):
        return self.user_set.all()

    class Meta:
        # Translators: Model name for Task(s)
        verbose_name = _('Tâche')
        verbose_name_plural = _('Tâches')

class VisualUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name=_("Date de naissance")),
    telephone = models.CharField(max_length=12, verbose_name=_("Numéro de téléphone"))
    tasks = models.ManyToManyField(Task, blank=True)

    def __str__(self):
        return self.user.first_name + self.user.last_name

    class Meta:
        # Translators: Model name for User(s)
        verbose_name = _('Utilisateur')
        verbose_name_plural = _('Utilisateurs')


