from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import VisualUser, Tag, Artist, VideoArtwork, ImageArtwork, SoundArtwork, Artwork

# Register your models here.

#VIUALUSER
admin.site.register(VisualUser)

#TAG
admin.site.register(Tag)

#ARTWORK
#@TODO Create interfaces for each child type adding custom fields.
class ArtworkChildAdmin(PolymorphicChildModelAdmin):
     base_model = Artwork

class ArtworkParentModel(PolymorphicParentModelAdmin):
    base_model = Artwork

    def get_child_models(self):
        return [(SoundArtwork,ArtworkChildAdmin), (VideoArtwork, ArtworkChildAdmin), (ImageArtwork, ArtworkChildAdmin)]

admin.site.register(Artwork, ArtworkParentModel)


#ARTIST
admin.site.register(Artist)