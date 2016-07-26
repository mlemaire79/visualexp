from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView
from visualAdmin.models import Exposition, Artwork
from datetime import date

class Homepage(View):

    def get(self, request):
        current_expo = Exposition.get_current()
        time = date.today()
        context = {
            'current_expo': current_expo,
            'time': time,
        }
        template = loader.get_template('extends/homepage.html')
        return HttpResponse(template.render(context, request))

class Current(View):

    def get(self, request):
        current_expo = Exposition.get_current()
        context = {
            'current_expo': current_expo,
        }
        template = loader.get_template('extends/currexposition.html')
        return HttpResponse(template.render(context, request))

class Listing(View):

    def get(self, request):
        current_expo = Exposition.get_current()
        context = {
            'current_expo': current_expo,
        }
        template = loader.get_template('extends/listartworks.html')
        return HttpResponse(template.render(context, request))

class ArtworkFlashed(View):

    def get(self, request, *args, **kwargs):
        qr_artwork = Artwork.objects.get(artwork_id=kwargs['artwork'])
        context = {
            'qr_artwork': qr_artwork,
        }
        template = loader.get_template('extends/zoomartwork.html')
        return HttpResponse(template.render(context, request))
