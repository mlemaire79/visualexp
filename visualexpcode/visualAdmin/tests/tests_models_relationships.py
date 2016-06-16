from django.test import TestCase
from visualAdmin.models import *

class ManyToManyArtistArtworks(TestCase):
    """Setup function for tests, create Objects here ! """
    def setUp(self):
        #Artist1 has 2 artworks
        ar1 = Artist.objects.create(first_name="TestFN1",last_name="TestLN1", stage_name="TestSN1")
        #Artist2 has 1 artwork
        ar2 = Artist.objects.create(first_name='TestFN2', last_name="TestLN2", stage_name="TestSN2")
        #Artwork1 has 1 artist
        aw1 =VideoArtwork.objects.create(title="TitleAW1", description="DescriptionAW1", length=100)
        #Artwork2 has 2 artists
        aw2 = ImageArtwork.objects.create(title="TitleAW2", description="DescAW2")
        ar1.artworks.add(aw1)
        ar2.artworks.add(aw1)
        ar1.artworks.add(aw2)
        

    def test_getArtworkListFromArtist(self):
        artist1 = Artist.objects.get(first_name="TestFN1")
        artworkList = artist1.artworks.all()
        self.assertEqual(len(artworkList), 2)

        artist2 = Artist.objects.get(first_name="TestFN2")
        artworkList = artist2.artworks.all()
        self.assertEqual(len(artworkList), 1, "Artist 2 only has 1 artwork")


    def test_get_artwork_details_from_list(self):
        self.fail("Not implemented")


    def test_get_artists__from_artwork(self):
        self.fail("Not implemented")
