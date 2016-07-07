from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from visualAdmin.models import Artwork

class ArtworkTest(View):

    def get(self, request):
        artwork_list = Artwork.objects.all()
        template = loader.get_template('bootstrap_test.html')
        context = {
            'artwork_list': artwork_list,
        }
        return HttpResponse(template.render(context, request))
