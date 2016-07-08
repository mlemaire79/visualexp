from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import VisualUser, Tag, Artist, VideoArtwork, ImageArtwork, SoundArtwork, Artwork, Display, Exposition, Task
from parler.admin import TranslatableAdmin, TranslatableModelForm
from django.utils.translation import ugettext_lazy as _

# Register your models here.

#VISUALUSER
admin.site.register(VisualUser)

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