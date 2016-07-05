from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import VisualUser, Tag, VideoArtwork, ImageArtwork, SoundArtwork, Artwork, Artist

# Register your models here.

#VIUALUSER
admin.site.register(VisualUser)

#TAG
admin.site.register(Tag)

#ARTWORK
class ChildAdminArtwork(PolymorphicChildModelAdmin):
    base_model = Artwork

class AdminVideoArtwork(ChildAdminArtwork):
    base_model = VideoArtwork
    show_in_index = False

class ParentAdminArtwork(PolymorphicParentModelAdmin):
    base_model = Artwork
    child_models = (VideoArtwork)

admin.site.register(Artwork, ParentAdminArtwork)
admin.site.register(VideoArtwork, AdminVideoArtwork)

#ARTIST
admin.site.register(Artist)