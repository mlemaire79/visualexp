from django.test import TestCase
from visualAdmin.models import Artist

class TestsArtist(TestCase):

    def setUp(self):
        a1 = Artist.objects.create(first_name='first_name_NS', last_name='last_name_NS')
        artist_stage_name = Artist.objects.create(first_name='first_name_with', last_name='last_name_with', stage_name = 'stage_name')

    def test_get_display_name(self): 

        artist_no_stage_name = Artist.objects.get(first_name='first_name_NS')
        artist_with_stage_name = Artist.objects.get(first_name='first_name_with')

        self.assertEqual(artist_with_stage_name.get_display_name(), artist_with_stage_name.stage_name)
        self.assertEqual(artist_no_stage_name.get_display_name(), artist_no_stage_name.first_name+' '+artist_no_stage_name.last_name)