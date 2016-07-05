from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.


class ArtworkList(View):
	greeting = "Good Day"

	def get(self, request):
		return HttpResponse(self.greeting)