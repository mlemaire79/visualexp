from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View

class Admin(View):

    def get(self, request):
        template = loader.get_template('admin/connexion.html')
        return HttpResponse(template.render(request))
