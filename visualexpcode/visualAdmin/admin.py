from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.forms import ModelForm
from django.contrib.auth.models import User

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import VisualUser, Tag, Artist, VideoArtwork, ImageArtwork, SoundArtwork, Artwork, Display, Exposition, Task
from parler.admin import TranslatableAdmin, TranslatableModelForm
from django.utils.translation import ugettext_lazy as _

# Register your models here.

#VISUALUSER
# Inline Admin Descriptor for VisualUser
class VisualUserInline(admin.StackedInline):
    model = VisualUser
    can_delete = False
    verbose_name_plural=_('Informations Complémentaires')
# @TODO Finish Adding fields for user modification
# @TODO Insert Basic group & user data.
class UserAdmin(BaseUserAdmin):
    inlines = (VisualUserInline,)
    # change_form = CustomUserForm
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
    )

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
            'Infos Oeuvre',
            {'fields':['publication_date','tags']}
        ],
        [
            'Infos Oeuvre Sonore',
            {'fields':['file', 'length']}
        ],
    )

class ImageArtworkAdmin(TranslatableAdmin, PolymorphicChildModelAdmin):
    base_form = TranslatableModelForm
    base_model = Artwork
    base_fieldsets = (
        [
            'Infos Oeuvre',
            {'fields':['publication_date','tags']}
        ],
        [
            'Infos Oeuvre Sonore',
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
admin.site.register(Artist)
admin.site.register(Exposition)
admin.site.register(Display)
admin.site.register(Task)

#Translations 
# class ArtworkTranslatableAdmin(TranslatableAdmin):
#     pass
# admin.site.unregister(Artwork)
# admin.site.register(Artwork, ArtworkTranslatableAdmin)