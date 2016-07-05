from django.test import TestCase
from visualAdmin.models import Display,Exposition,Artwork
import time
class TestsDisplay(TestCase):

    def setUp(self):
        aw = SoundArtwork.objects.create(title="1", description="yolo", length="100")
        expo = Exposition.objects.create(title="Expo1", description="dec", author="author", start_date=time.strftime("%d/%m/%Y"), end_date=time.strftime("%d/%m/%Y"))
        display1 = Display.objects.create(artwork=aw, exposition=expo, deliveryTime=time.strftime("%c"))

    def test_get_artwork(self):
        self.fail("Not implemented")
    def test_add_view(self):
        self.fail("Not implemented")