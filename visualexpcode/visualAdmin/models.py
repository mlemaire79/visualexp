from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from itertools import chain
from datetime import date, timedelta
from polymorphic.models import PolymorphicModel
from parler.models import TranslatableModel, TranslatedFields
#from parler.managers import TranslatableManager
from .managers import ArtworkManager
from .validators import validate_sound_file_extension, validate_video_file_extension
from django.utils.safestring import mark_safe
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

    def __unicode__(self):
        return u"%s" % (self.name)


    def get_artworks(self):
        return list(chain(self.videoartwork_set.all(),self.imageartwork_set.all(),self.soundartwork_set.all()))

    def get_artists(self):
        return list(chain(self.artist_set.all()))

        class Meta:
            # Translators: Model name for Tag(s)
            verbose_name = _('Etiquette')
            verbose_name_plural = _('Etiquettes')

class Artist(TranslatableModel):
    artist_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64, verbose_name=_("Prénom"))
    last_name = models.CharField(max_length=64, verbose_name=_("Nom"))
    stage_name = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("Pseudonyme"))
    birth_date = models.DateField(blank=True, null=True, verbose_name=_("Date de naissance"))
    tags = models.ManyToManyField(Tag, blank = True)
    translations = TranslatedFields(
            description = models.TextField(verbose_name = _('Biographie'), blank=True, null=True)
        )
    photo = models.ImageField(blank = True, null= True, verbose_name=_('Photo de l\'Artiste'), upload_to='image/', max_length=255)

    def get_display_name(self):
        if not self.stage_name is None and not self.stage_name == '':
            return self.stage_name
        else:
            return self.first_name +' '+ self.last_name
    # Translators : Column Name for artist display name in admin
    get_display_name.short_description = _("Artiste")

    def image_tag(self):
        """Return img markup for display in admin"""
        if not self.photo == '':
            return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.photo))
        else:
            return ''
    image_tag.short_description = _('Prévisualisation (Après Enregistrement)')


    def __str__(self):
        return self.get_display_name()

    class Meta:
        # Translators: Model name for Artist(s)
        verbose_name = _('Artiste')
        verbose_name_plural = _('Artistes')

"""Abstract Model for the artworks"""
class Artwork(PolymorphicModel, TranslatableModel):

    objects = ArtworkManager()

    artwork_id = models.AutoField(primary_key=True)

    translations = TranslatedFields (
        title = models.CharField(max_length=255, verbose_name=_("Titre de l'oeuvre")), #Max supported by MySql text field
        description = models.TextField(blank=True, verbose_name=_("Description de l'oeuvre")),
    )
    publication_date = models.DateField(blank=True, null=True, verbose_name=_("Date de publication"))
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    #@TODO Dimensions, coordinates ?

    def __str__(self):
        return self.title

    def get_type(self):
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
                    return _("Autre")
                else:
                    return _("Image")
            else:
                return _("Vidéo")
        else:
            return _("Son")
    # Translators : Column Name for Artwork display type in admin
    get_type.short_description = _("Type d'Oeuvre")

    class Meta:
        # Translators: Model name for Artwork
        verbose_name = _('Oeuvre')
        verbose_name_plural = _('Oeuvres')



class VideoArtwork(Artwork):
    #artwork = models.ForeignKey()
    length = models.IntegerField(_("Durée (En secondes)"), blank=True, null=True)
    file = models.FileField(upload_to='video/', verbose_name=_("Vidéo"), validators=[validate_video_file_extension])

    class Meta:
        # Translators: Model name for VideoArtwork(s)
        verbose_name = _('Oeuvre Vidéo')
        verbose_name_plural = _('Oeuvres Vidéo')

class ImageArtwork(Artwork):
    file = models.ImageField(upload_to='image/', verbose_name=_("Image"))

    class Meta:
        # Translators: Model name for ImageArtwork(s)
        verbose_name = _('Oeuvre Image')
        verbose_name_plural = _('Oeuvres Image')

class SoundArtwork(Artwork):
    length = models.IntegerField(_("Durée (en secondes)"), blank=True, null=True)
    file = models.FileField(upload_to='audio/', verbose_name=_("Son"), validators=[validate_sound_file_extension])

    class Meta:
        # Translators: Model name for SoundArtwork(s)
        verbose_name = _('Oeuvre Sonore')
        verbose_name_plural = _('Oeuvres Sonore')

#@TODO Add opening/closing hours
class Exposition(TranslatableModel):
    #Number of days separating expositions
    DAYS_BETWEEN = 2

    expo_id = models.AutoField(primary_key=True)
    translations = TranslatedFields (
        title = models.CharField(max_length=64, verbose_name=_("Titre de l'exposition")),
        description = models.TextField(verbose_name=_("Description")),
    )
    author = models.CharField(max_length=64, blank=True, verbose_name=_("Auteur de l'exposition"))
    start_date = models.DateField(verbose_name=_("Début de l'exposition"))
    end_date = models.DateField(verbose_name=_("Fin de l'exposition"))
    artworks = models.ManyToManyField(Artwork, through='Display')
    image = models.ImageField(blank = True, null= True, upload_to='image/', verbose_name=_("Affiche de l'Exposition"))

    def clean(self):
        """
         - Start date sould be before end date
         - Expositions should not overlap 
           and have Exposition.DAYS_BETWEEN days off between each of them
        """

        #Check for start/end dates
        if self.start_date > self.end_date:
            raise ValidationError({
                'end_date':_('La date de fin doit etre postérieure à la date de début.'),
                'start_date': _('La date de début doit etre antérieure à la date de fin.')})

        #Check for overlap - days off
        expos = Exposition.objects.all()
        for existing in expos:
            #Overlap
            overlap_msg = _("Ces dates sont en conflit avec l'exposition %(exposition)s. Veuillez les changer.") % {'exposition': existing.title} 
            turnaround_msg = _(" avec l'exposition %(exposition)s. Veuillez les changer.") % {'exposition': existing.title} 

            if self.start_date > existing.start_date and self.end_date < existing.end_date:
                raise ValidationError({
                    'start_date': overlap_msg,
                    'end_date': overlap_msg
                    })
            if self.start_date < existing.start_date and self.end_date > existing.end_date:
                raise ValidationError({
                    'start_date': overlap_msg,
                    'end_date': overlap_msg
                    })
            if self.start_date > existing.start_date and self.start_date < existing.end_date:
                raise ValidationError({
                    'start_date': overlap_msg
                    })
            if self.end_date > existing.start_date and self.end_date < existing.end_date:
                raise ValidationError({
                    'end_date': overlap_msg
                    })
            #Days off
            if existing.end_date - self.start_date >= timedelta(-2) and existing.end_date - self.start_date < timedelta(0):
                raise ValidationError({
                    'start_date': _("Veuillez laisser au moins %(nb_days)s jours apres la fin de l'exposition %(exposition)s") % {'nb_days': Exposition.DAYS_BETWEEN, 'exposition': existing.title}
                    })
            if existing.start_date - self.end_date <= timedelta(1) and existing.start_date - self.end_date > timedelta(0):
                raise ValidationError({
                    'start_date': _("Veuillez laisser au moins %(nb_days)s jours avant le début de l'exposition %(exposition)s") % {'nb_days': Exposition.DAYS_BETWEEN, 'exposition': existing.title}
                    })


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
    position = models.IntegerField(default=1, verbose_name=_("Emplacement"))
    nb_views = models.IntegerField(default=0, verbose_name=_("Nombre de vues"))
    delivery_time = models.TimeField(blank=True,null=True, verbose_name=_("Date de livraison"))
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

class VisualUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name=_("Date de naissance")),
    telephone = models.CharField(max_length=12, verbose_name=_("Numéro de téléphone"))


    def __str__(self):
        return self.user.first_name + self.user.last_name

    def __unicode__(self):
        return u"%s" % (self.str())

    class Meta:
        # Translators: Model name for User(s)
        verbose_name = _('Utilisateur')
        verbose_name_plural = _('Utilisateurs')

class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    exposition= models.ForeignKey(Exposition, on_delete=models.CASCADE)
    start_date=models.DateTimeField(verbose_name=_("Début de la tâche"))
    end_date=models.DateTimeField(verbose_name=_("Fin de la tâche"))
    name = models.CharField(max_length=64, verbose_name=_("Nom de la tâche"))
    description = models.TextField(blank=True, verbose_name=_("Description de la tâche"))
    users = models.ManyToManyField(User, blank=True, verbose_name=_("Utilisateurs assignés"))
    is_completed = models.BooleanField(default=False, verbose_name='Tache Finie')

    def __str__ (self):
        return self.name

    def get_users(self):
        return ", ".join([u.username for u in self.users.all()])
    get_users.short_description = _("Utilisateurs Assignés")

    def clean(self):
        """
        Start date sould be before end date
        """
        if self.start_date > self.end_date:
            raise ValidationError({
                'end_date':_('La date de fin doit etre postérieure à la date de début.'),
                'start_date': _('La date de début doit etre antérieure à la date de fin.')})

    class Meta:
        # Translators: Model name for Task(s)
        verbose_name = _('Tâche')
        verbose_name_plural = _('Tâches')




