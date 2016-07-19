from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from datetime import date

from visualAdmin.models import Exposition

class ExpoListView(View):

    def get(self, request):
        next_expos_list = Exposition.objects.filter(start_date__gte=date.today())

        context = {
            'next_expos_list': next_expos_list,
        }
        return render(request, 'admin/visualAdmin/display/choose_expo.html', context)