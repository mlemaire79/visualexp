from django.test import TestCase
from visualAdmin.models import Artwork,VideoArtwork,ImageArtwork,SoundArtwork, Artist

class TestsArtwork(TestCase):

    def setUp(self):
        ar = Artist.objects.create(first_name="Ar", last_name="Tist")

        aw1 = SoundArtwork.objects.create(title="1", artist = ar, description="desc1", length="100")
        aw2 = VideoArtwork.objects.create(title="2", artist= ar, description="desc2", length="100")
        aw3 = ImageArtwork.objects.create(title="3", artist = ar, description="desc3")

    def test_get_artwork_type(self):
        aw = SoundArtwork.objects.get()
        self.assertEqual(aw.get_type(), "Son")

        aw = VideoArtwork.objects.get()
        self.assertEqual(aw.get_type(), "Vidéo")

        aw = ImageArtwork.objects.get()
        self.assertEqual(aw.get_type(), "Image")
        

