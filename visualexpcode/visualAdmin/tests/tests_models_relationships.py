from django.test import TestCase
from visualAdmin.models import *

class ManyToManyArtistArtworks(TestCase):
	"""Setup function for tests, create Objects here ! """
	def setUp(self):
		ar1 = Artist.objects.create(first_name="TestFN1",last_name="TestLN1", stage_name="TestSN1")
		ar2 = Artist.objects.create(first_name='TestFN2', last_name="TestLN2", stage_name="TestSN2")
		aw1 =VideoArtwork.objects.create(title="TitleAW1", description="DescriptionAW1", length=100)
		aw2 = ImageArtwork.objects.create(title="TitleAW2", description="DescAW2")
		aw1.artists.add(ar1)
		aw2.artists.add(ar1)
		aw2.artists.add(ar2)

	def test_getArtworkListFromArtist(self):
		artist1 = Artist.objects.get(first_name="TestFN1")
		#Artist 1 should have 2 artworks
		self.assertEquals(len(artist1.get_artworks()), 2)

		artist2 = Artist.objects.get(first_name="TestFN2")
		#Artist 2 should only have one artwork
		self.assertEquals(len(artist2.get_artworks()), 1)

	#TODO
	def test_get_artwork_details_from_list(self):
		assert False, "Test not implemented"

	#TODO
	def test_get_artwork_type_from__list(self):
		assert False, "Test not implemented"

