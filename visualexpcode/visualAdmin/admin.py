# @TODO Fix Imports ( que bordel !)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import VisualUser, Tag, Artist, VideoArtwork, ImageArtwork, SoundArtwork, Artwork, Display, Exposition, Task
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
    base_fieldsets = (
        [
            _('Infos Oeuvre'),
            {'fields':['publication_date','tags']}
        ],
        [
            'Infos Oeuvre Sonore',
            {'fields':['file', 'length']}
        ],
    )


class VideoArtworkAdmin(TranslatableAdmin, PolymorphicChildModelAdmin):
    base_form = TranslatableModelForm
    base_model = Artwork
    base_fieldsets = (
        [
            _('Infos Oeuvre'),
            {'fields':['publication_date','tags']}
        ],
        [
            _('Infos Oeuvre Sonore'),
            {'fields':['file', 'length']}
        ],
    )

class ImageArtworkAdmin(TranslatableAdmin, PolymorphicChildModelAdmin):
    base_form = TranslatableModelForm
    base_model = Artwork
    base_fieldsets = (
        [
            _('Infos Oeuvre'),
            {'fields':['publication_date','tags']}
        ],
        [
            _('Infos Oeuvre Sonore'),
            {'fields':['file']}
        ],
    )

class ArtworkParentModel(TranslatableAdmin, PolymorphicParentModelAdmin):
    base_form = TranslatableModelForm
    base_model = Artwork
    list_display = ('title', 'description',)

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
                (_('Oeuvres'), {
                    'fields': ('artworks',)
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
admin.site.register(Exposition)
admin.site.register(Display)
admin.site.register(Task)

#Translations 
# class ArtworkTranslatableAdmin(TranslatableAdmin):
#     pass
# admin.site.unregister(Artwork)
# admin.site.register(Artwork, ArtworkTranslatableAdmin)