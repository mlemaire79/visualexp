# @TODO Fix Imports ( que bordel !)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import VisualUser, Tag, Artist, VideoArtwork, ImageArtwork, SoundArtwork, Artwork, Display, Exposition, Task
from datetime import date, timedelta
from parler.admin import TranslatableAdmin, TranslatableModelForm
from tinymce.widgets import TinyMCE
from django.utils.translation import ugettext_lazy as _

# Register your models here.

#VISUALUSER
# Inline Admin Descriptor for VisualUser
class VisualUserInline(admin.StackedInline):
    model = VisualUser
    can_delete = False
    verbose_name_plural=_('Informations Complémentaires')

# @TODO Insert Basic group & user data.
class UserAdmin(BaseUserAdmin):
    inlines = []
    list_display = ('username', 'last_name', 'first_name', 'email', 'last_login' )
    list_filter = ('groups', 'last_login')
    search_fields = ('username', 'last_name')

    def get_fieldsets(self, request, obj=None, **kwargs):
        """Override this method in order to get custom fieldsets according to roles """
        if not obj: 
            return super(UserAdmin,self).get_fieldsets(request, None)
        if request.user.is_superuser:
            fieldsets = (
                (None, {
                    'fields': ('username', 'password')
                }),
                (_('Informations Utilisateur'), {
                    'fields': ('first_name', 'last_name', 'email')
                }),
                (_('Groupes'), {
                    'fields': ('groups', 'user_permissions')
                    }),
                (_('Informations Admin'), {
                    'fields': ('is_active', 'is_staff', 'last_login', 'date_joined')
                    }),
            )
        else:
            fieldsets = (
                (None, {
                    'fields': ('username', 'password')
                }),
                (_('Informations Utilisateur'), {
                    'fields': ('first_name', 'last_name', 'email')
                }),
                (_('Groupes'), {
                    'fields': ('groups',)
                    }),
            )
        return fieldsets

    def add_view(self, request, form_url='', extra_context=None):
        self.inlines = []
        self.fieldsets = self.get_fieldsets(request)
        return super(UserAdmin,self).add_view(request,form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        #self.fieldsets = self.get_fieldsets(request)
        self.inlines = (VisualUserInline,)
        return super(UserAdmin,self).change_view(request,object_id, form_url, extra_context)

    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        obj.is_active = True
        obj.save()


#Reregister user in admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#TAG
class TranslatableTag(TranslatableAdmin):
    pass

admin.site.register(Tag, TranslatableTag)

#ARTWORK
class SoundArtworkAdmin(TranslatableAdmin, PolymorphicChildModelAdmin):
    base_form = TranslatableModelForm
    base_model = Artwork
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }
    base_fieldsets = (
        [
            _('Infos Oeuvre Sonore'),
            {'fields':['title', 'artist', 'file']}
        ],
        [
            _('Informations Complémentaires'),
            {'fields':['description', 'length', 'publication_date', 'tags',]}
        ],
    )

    def save_model(self, request, obj, form, change):
        """ Delete old file when replacing sound """

        try:
            old = SoundArtwork.objects.get(artwork_id=obj.artwork_id)
            if old.file != obj.file:
                old.file.delete(save=False)
        except: pass # When new file do nothing
        obj.save()

    def delete_model(self, request, obj):
        try:
            old = SoundArtwork.objects.get(artwork_id=obj.artwork_id)
            old.file.delete(save=False)
        except: pass # When no file do nothing
        obj.delete()


class VideoArtworkAdmin(TranslatableAdmin, PolymorphicChildModelAdmin):
    base_form = TranslatableModelForm
    base_model = Artwork
    base_fieldsets = (
        [
            _('Infos Oeuvre Sonore'),
            {'fields':['title', 'artist', 'file']}
        ],
        [
            _('Informations Complémentaires'),
            {'fields':['description', 'length', 'publication_date', 'tags',]}
        ],
    )

    def save_model(self, request, obj, form, change):
        """ Delete old file when replacing sound """

        try:
            old = VideoArtwork.objects.get(artwork_id=obj.artwork_id)
            if old.file != obj.file:
                old.file.delete(save=False)
        except: pass # When new file do nothing
        obj.save()

    def delete_model(self, request, obj):
        try:
            old = VideoArtwork.objects.get(artwork_id=obj.artwork_id)
            old.file.delete(save=False)
        except: pass # When no file do nothing
        obj.delete()

class ArtworkTypeFilter(admin.SimpleListFilter):
    """
    Set a custom filter for Artwork by type
    """
    # Translators : Filter for exposition in admin interface
    title = _('Type')

    parameter_name = 'get_type'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar
        """
        return (
            ('Image', _('Image')),
            ('Son', ('Son')),
            ('Video', ('Vidéo')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """

        if self.value() == 'Image':
            return ImageArtwork.objects.all()
        if self.value() == 'Son':
            return SoundArtwork.objects.all()
        if self.value() == 'Vidéo':
            return VideoArtwork.objects.all()

class ImageArtworkAdmin(TranslatableAdmin, PolymorphicChildModelAdmin):
    base_form = TranslatableModelForm
    base_model = Artwork
    base_fieldsets = (
    [
        _('Infos Oeuvre Sonore'),
        {'fields':['title', 'artist', 'file']}
    ],
    [
        _('Informations Complémentaires'),
        {'fields':['description', 'publication_date', 'tags',]}
    ],
)

    def save_model(self, request, obj, form, change):
        """ Delete old file when replacing sound """

        try:
            old = ImageArtwork.objects.get(artwork_id=obj.artwork_id)
            if old.file != obj.file:
                old.file.delete(save=False)
        except: pass # When new file do nothing
        obj.save()

    def delete_model(self, request, obj):
        try:
            old = ImageArtwork.objects.get(artwork_id=obj.artwork_id)
            old.file.delete(save=False)
        except: pass # When no file do nothing
        obj.delete()

class ArtworkParentModel(TranslatableAdmin, PolymorphicParentModelAdmin):
    base_form = TranslatableModelForm
    base_model = Artwork
    list_display = ('title', 'artist', 'get_type')
    list_filter = (ArtworkTypeFilter,)
    search_fields = ('translations__title', 'artist__first_name', 'artist__last_name', 'artist__stage_name')


    def get_child_models(self):
        return [
            (SoundArtwork,SoundArtworkAdmin),
            (VideoArtwork, VideoArtworkAdmin),
            (ImageArtwork, ImageArtworkAdmin)
        ]

admin.site.register(Artwork, ArtworkParentModel)

#ARTIST
class ArtistAdmin(TranslatableAdmin):
    base_form = TranslatableModelForm
    base_model = Artist
    list_display = ('get_display_name','last_name', 'first_name',)
    search_fields = ('first_name', 'last_name', 'stage_name')
    list_filter = ('tags',)
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }
    fieldsets = (
                (_("Informations sur l'Artiste"), {
                    'fields': ('first_name', 'last_name', 'stage_name', 'birth_date', 'tags')
                }),
                (_('Affichage'), {
                    'fields': ('description','photo', 'image_tag')
                    }),
            )
    # fields= ('image_tag',)
    readonly_fields = ('image_tag',)

    def save_model(self, request, obj, form, change):
        """ Delete old file when replacing photo """

        try:
            old = Artist.objects.get(artist_id=obj.artist_id)
            if old.photo != obj.photo:
                old.photo.delete(save=False)
        except: pass # When new photo do nothing
        obj.save()

    def delete_model(self, request, obj):
        try:
            old = Artist.objects.get(artist_id=obj.artist_id)
            old.photo.delete(save=False)
        except: pass # When no photo do nothing
        obj.delete()

admin.site.register(Artist, ArtistAdmin)

#Exposition
class StartDateExpositionListFilter(admin.SimpleListFilter):
    """
    Set a custom filter for exposition by start_date
    """
    # Translators : Filter for exposition in admin interface
    title = _('Date de Début')

    parameter_name = 'start_date'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar
        """
        return (
            ('following', _('Expositions à venir')),
            ('week', ('Cette Semaine')),
            ('month', ('Ce Mois-ci')),
            ('year', ('Cette Année')),
            ('nextyear', ("L'an prochain"))
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        today = date.today()
        #isocalendar : Return a 3-tuple, (ISO year, ISO week number, ISO weekday) weekday starts at sunday = 0
        isocal = date.isocalendar(today)
        curr_year = today.year
        curr_month = today.month
        week_beginning = today- timedelta(days=date.isocalendar(today)[2])
        week_end = today + timedelta(days=(6 - date.isocalendar(today)[2]))


        if self.value() == 'following':
            return queryset.filter(start_date__gte=today)
        if self.value() == 'week':
            return queryset.filter(start_date__range=(week_beginning, week_end))
        if self.value() == 'month':
            return queryset.filter(start_date__month=curr_month)
        if self.value() == 'year':
            return queryset.filter(start_date__year=2016)
        if self.value() == 'nextyear':
            return queryset.filter(start_date__year=curr_year+1)

class EndDateExpositionListFilter(admin.SimpleListFilter):
    """
    Set a custom filter for exposition by end date
    """
    # Translators : Filter for exposition in admin interface
    title = _('Date de Fin')

    parameter_name = 'end_date'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar
        """
        return (
            ('ended', _('Expositions terminées')),
            ('week', ('Cette Semaine')),
            ('month', ('Ce Mois-ci')),
            ('year', ('Cette Année')),
            ('nextyear', ("L'an prochain"))
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        today = date.today()
        #isocalendar : Return a 3-tuple, (ISO year, ISO week number, ISO weekday) weekday starts at sunday = 0
        isocal = date.isocalendar(today)
        curr_year = today.year
        curr_month = today.month
        week_beginning = today- timedelta(days=date.isocalendar(today)[2])
        week_end = today + timedelta(days=(6 - date.isocalendar(today)[2]))


        if self.value() == 'ended':
            return queryset.filter(end_date__lt=today)
        if self.value() == 'week':
            return queryset.filter(end_date__range=(week_beginning, week_end))
        if self.value() == 'month':
            return queryset.filter(end_date__month=curr_month)
        if self.value() == 'year':
            return queryset.filter(end_date__year=2016)
        if self.value() == 'nextyear':
            return queryset.filter(end_date__year=curr_year+1)


class ExpositionAdmin(TranslatableAdmin):
    base_form = TranslatableModelForm
    base_model = Exposition
    list_display = ('title', 'start_date', 'end_date', 'author')
    search_fields = ('translations__title','author')
    list_filter = (StartDateExpositionListFilter, EndDateExpositionListFilter)
    fields = ('title', 'author', 'start_date', 'end_date', 'description')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }


admin.site.register(Exposition, ExpositionAdmin)
admin.site.register(Display)
admin.site.register(Task)

#Translations 
# class ArtworkTranslatableAdmin(TranslatableAdmin):
#     pass
# admin.site.unregister(Artwork)
# admin.site.register(Artwork, ArtworkTranslatableAdmin)