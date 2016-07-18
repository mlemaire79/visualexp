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
        # aw1 =VideoArtwork.objects.create(title="TitleAW1", description="DescriptionAW1", length=100)
        # #Artwork2 has 2 artists
        # aw2 = ImageArtwork.objects.create(title="TitleAW2", description="DescAW2")
        # ar1.artworks.add(aw1)
        # ar2.artworks.add(aw1)
        # ar1.artworks.add(aw2)
        

    # def test_getArtworkListFromArtist(self):
    #     artist1 = Artist.objects.get(first_name="TestFN1")
    #     artworkList = artist1.artworks.all()
    #     self.assertEqual(len(artworkList), 2)

    #     artist2 = Artist.objects.get(first_name="TestFN2")
    #     artworkList = artist2.artworks.all()
    #     self.assertEqual(len(artworkList), 1, "Artist 2 only has 1 artwork")


    def test_get_artwork_details_from_list(self):
        self.fail("Not implemented")


    def test_get_artists__from_artwork(self):
        self.fail("Not implemented")
        
class ManyToManyTagArtists(TestCase):
	"""Test unitaire entre les tags et les artistes"""
	def setUp(self):
		tg1 = Tag.objects.create(name="Contemporain", description="Description tag1")
		tg2 = Tag.objects.create(name="Baroque", description="Description tag2")
		ar1 = Artist.objects.create(first_name="TaggedArtist1", last_name="TaggedArtist1", stage_name="Pseudo1")
		ar2 = Artist.objects.create(first_name="TaggedArtist2", last_name="TaggedArtist2", stage_name="Pseudo2")
		ar1.tags.add(tg1, tg2)
		ar2.tags.add(tg2)

	# def test_getArtistListFromTag(self):
	# 	tag1 = Tag.objects.get(name="Contemporain")
	# 	artistList = tg1.artists.all()
	# 	#Ici la catégorie Contemporain devrait lister 2 artistes
	# 	self.assertEquals(len(artistList), 1)
		
	# 	tag2 = Tag.objects.get(name="Baroque")
	# 	artistList = tg2.artists.all()
	# 	#Ici la catégorie Baroque devrait lister 1 artistes
	# 	self.assertEquals(len(artistList), 2)

	def test_get_artist_details_from_list(self):
		assert False, "Pas fait"

class ManyToManyTagArtworks(TestCase):
	"""Test unitaire entre les tags et les artworks"""
    # @TODO Fix
	# def setUp(self):
	# 	tg1 = Tag.objects.create(name="Abstrait", description="Description abstrait")
	# 	tg2 = Tag.objects.create(name="Podcast", description="DEscription podcast")
	# 	aw1 = ImageArtwork.objects.create(title="TaggedArtwork1", description="TaggedArtwork1")
	# 	aw2 = VideoArtwork.objects.create(title="TaggedArtwork2", description="TaggedArtwork2", length=100)
	# 	aw1.tags.add(tg1, tg2)
	# 	aw2.tags.add(tg2)
	
	# def test_getArtworkListFromTag(self):
	# 	tag1 = Tag.objects.get(name="Abstrait")
	# 	artworkList = tg1.artworks.all()
	# 	#Ici la catégorie Abstrait devrait lister 2 oeuvres
	# 	self.assertEquals(len(artworkList), 1)

	# 	tag2 = Tag.objects.get(name="Podcast")
	# 	artworkList = tg2;artworks.all()
	# 	#Ici la catégorie podcast devrait lister 1 oeuvres
	# 	self.assertEquals(len(artworkList), 2)

	def test_get_artwork_details_from_list(self):
		assert False, "Pas fait"