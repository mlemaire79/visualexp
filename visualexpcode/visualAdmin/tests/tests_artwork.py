from django.test import TestCase
from visualAdmin.models import Artwork,VideoArtwork,ImageArtwork,SoundArtwork

class TestsArtwork(TestCase):

    def setUp(self):
        aw1 = SoundArtwork.objects.create(title="1", description="desc1", length="100")
        aw2 = VideoArtwork.objects.create(title="2", description="desc2", length="100")
        aw3 = ImageArtwork.objects.create(title="3", description="desc3")

    # @TODO : Fix
    # def test_get_artwork_type(self):
    #     aw1 = Artwork.objects.get(title="1")
    #     aw2 = Artwork.objects.get(title="2")
    #     aw3 = Artwork.objects.get(title="3")

    #     self.assertEqual(aw1.getType(), "sound")

    #     self.assertEqual(aw2.getType(), "video")
        
    #     self.assertEqual(aw3.getType(), "image")