from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView
from visualAdmin.models import Exposition
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
