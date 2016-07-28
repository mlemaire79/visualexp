from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView
from visualAdmin.models import Exposition, Artwork, Display, Artist
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
        current_expo = Exposition.get_current()
        qr_artwork = Artwork.objects.get(artwork_id=kwargs['artwork'])
        try:
            qr_display = Display.objects.get(artwork=qr_artwork, exposition=current_expo)
        except Display.DoesNotExist:
            redirect = True
            time = date.today()
            context = {
                'current_expo': current_expo,
                'time': time,
                'redirect': redirect,
            }
            return render(request, 'extends/homepage.html', context)
    
        qr_display.nb_views = qr_display.nb_views+1
        qr_display.save()
        context = {
            'qr_artwork': qr_artwork,
            'qr_display': qr_display,
        }
        template = loader.get_template('extends/zoomartwork.html')
        return HttpResponse(template.render(context, request))

class ArtistAsked(View):

    def get(self, request, *args, **kwargs):
        asked_artist = Artist.objects.get(artist_id=kwargs['artist'])
        back = request.GET.get('back', None)
        context = {
            'asked_artist': asked_artist,
            'back': back,
        }
        template = loader.get_template('extends/zoomartist.html')
        return HttpResponse(template.render(context, request))

class Map(View):

    def get(self, request):
        current_expo = Exposition.get_current()
        display_expo = Display.objects.filter(exposition=current_expo)
        context = {
            'current_expo': current_expo,
            'display_expo': display_expo,
        }
        template = loader.get_template('extends/mapexposition.html')
        return HttpResponse(template.render(context, request))