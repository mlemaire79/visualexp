from django.test import TestCase
from visualAdmin.models import *

#Commande pour Cédric : python ../../manage.py test

class ManyToManyArtistArtworks(TestCase):
	"""Setup function for tests, create Objects here ! """
	def setUp(self):
		ar1 = Artist.objects.create(first_name="TestFN1",last_name="TestLN1", stage_name="TestSN1")
		ar2 = Artist.objects.create(first_name='TestFN2', last_name="TestLN2", stage_name="TestSN2")
		aw1 = VideoArtwork.objects.create(title="TitleAW1", description="DescriptionAW1", length=100)
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

class ManyToManyTagArtists(TestCase):
	"""Test unitaire entre les tags et les artistes"""
	def setUp(self):
		tg1 = Tag.objects.create(name="Contemporain", description="Description tag1")
		tg2 = Tag.objects.create(name="Baroque", description="Description tag2")
		ar1 = Artist.objects.create(first_name="TaggedArtist1", last_name="TaggedArtist1", stage_name="Pseudo1")
		ar2 = Artist.objects.create(first_name="TaggedArtist2", last_name="TaggedArtist2", stage_name="Pseudo2")
		ar1.tags.add(tg1, tg2)
		ar2.tags.add(tg2)

	def test_getArtistListFromTag(self):
		tag1 = Tag.objects.get(name="Contemporain")
		#Ici la catégorie Contemporain devrait lister 2 artistes
		self.assertEquals(len(tag1.get_artists()), 1)
		
		tag2 = Tag.objects.get(name="Baroque")
		#Ici la catégorie Baroque devrait lister 1 artistes
		self.assertEquals(len(tag2.get_artists()), 2)

	#TODO
	def test_get_artist_details_from_list(self):
		assert False, "Pas fait"

class ManyToManyTagArtworks(TestCase):
	"""Test unitaire entre les tags et les artworks"""
	def setUp(self):
		tg1 = Tag.objects.create(name="Abstrait", description="Description abstrait")
		tg2 = Tag.objects.create(name="Podcast", description="DEscription podcast")
		aw1 = ImageArtwork.objects.create(title="TaggedArtwork1", description="TaggedArtwork1")
		aw2 = VideoArtwork.objects.create(title="TaggedArtwork2", description="TaggedArtwork2", length=100)
		aw1.tags.add(tg1, tg2)
		aw2.tags.add(tg2)
	
	def test_getArtworkListFromTag(self):
		tag1 = Tag.objects.get(name="Abstrait")
		#Ici la catégorie Abstrait devrait lister 2 oeuvres
		self.assertEquals(len(tag1.get_artworks()), 1)

		tag2 = Tag.objects.get(name="Podcast")
		#Ici la catégorie podcast devrait lister 1 oeuvres
		self.assertEquals(len(tag2.get_artworks()), 2)

	#TODO
	def test_get_artwork_details_from_list(self):
		assert False, "Pas fait"