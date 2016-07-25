from django.test import TestCase
from visualAdmin.models import Exposition
from datetime import date, timedelta, datetime

class TestsExposition(TestCase):

    #def setUp(self):
        #dtest = date.today()
        #expo1 = Exposition.objects.create(title="TestExpo", description="test", author="Cedric", start_date= dtest, end_date=dtest)
        #expo2 = Exposition objects.create(title="TestExpo2", description="test2", author="Cedric", start_date= dtest, end_date=dtest)
        #expo3 = Exposition objects.create(title="TestExpo3", description="test3", author="Cedric", start_date= dtest, end_date=dtest)

    #def get_expo_ordered(self):
        #expo = Exposition.get_current()
        #self.assertEqual(expo.title, "TestExpo")