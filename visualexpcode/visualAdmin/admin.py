from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import VisualUser, Tag, Artist, VideoArtwork, ImageArtwork, SoundArtwork, Artwork, Display, Exposition, Task

# Register your models here.

#VISUALUSER
admin.site.register(VisualUser)

#TAG
admin.site.register(Tag)

#ARTWORK
<<<<<<< HEAD
#class ChildAdminArtwork(PolymorphicChildModelAdmin):
    #base_model = Artwork

#class AdminVideoArtwork(ChildAdminArtwork):
    #base_model = VideoArtwork
    #show_in_index = False

#class ParentAdminArtwork(PolymorphicParentModelAdmin):
    #base_model = Artwork
    #child_models = (VideoArtwork)

#admin.site.register(Artwork, ParentAdminArtwork)
#admin.site.register(VideoArtwork, AdminVideoArtwork)
=======
class SoundArtworkAdmin(PolymorphicChildModelAdmin):
    base_model = Artwork
    base_fieldsets = (
        [
            'Infos Oeuvre',
            {'fields':['title','description','publication_date','tags']}
        ],
        [
            'Infos Oeuvre Sonore',
            {'fields':['file', 'length']}
        ],
    )

class VideoArtworkAdmin(PolymorphicChildModelAdmin):
    base_model = Artwork
    base_fieldsets = (
        [
            'Infos Oeuvre',
            {'fields':['title','description','publication_date','tags']}
        ],
        [
            'Infos Oeuvre Sonore',
            {'fields':['file', 'length']}
        ],
    )

class ImageArtworkAdmin(PolymorphicChildModelAdmin):
    base_model = Artwork
    base_fieldsets = (
        [
            'Infos Oeuvre',
            {'fields':['title','description','publication_date','tags']}
        ],
        [
            'Infos Oeuvre Sonore',
            {'fields':['file']}
        ],
    )

class ArtworkParentModel(PolymorphicParentModelAdmin):
    base_model = Artwork

    def get_child_models(self):
        return [
            (SoundArtwork,SoundArtworkAdmin),
            (VideoArtwork, VideoArtworkAdmin),
            (ImageArtwork, ImageArtworkAdmin)
        ]

admin.site.register(Artwork, ArtworkParentModel)

>>>>>>> origin/master

#ARTIST
admin.site.register(Artist)
admin.site.register(Exposition)
admin.site.register(Display)
admin.site.register(Task)