from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View

class Homepage(View):

    def get(self, request):
        template = loader.get_template('extends/homepage.html')
        return HttpResponse(template.render(request))

class Current(View):

    def get(self, request):
        template = loader.get_template('extends/currexposition.html')
        return HttpResponse(template.render(request))

class Listing(View):

    def get(self, request):
        template = loader.get_template('extends/listartworks.html')
        return HttpResponse(template.render(request))
