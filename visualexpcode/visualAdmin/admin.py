from django.contrib import admin

# Register your models here.

#VIUALUSER
from .models import VisualUser
admin.site.register(VisualUser)

#TAG
from .models import Tag
admin.site.register(Tag)

#ARTWORK
from .models import Artwork
admin.site.register(Artwork)

from .models import VideoArtwork
admin.site.register(VideoArtwork)

from .models import ImageArtwork
admin.site.register(ImageArtwork)

from .models import SoundArtwork
admin.site.register(SoundArtwork)

#ARTIST
from .models import Artist
admin.site.register(Artist)