# from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.views.generic import View
from parler.views import TranslatableModelFormMixin
from visualAdmin.forms.manageexpo import AddDisplayForm

from datetime import date

from visualAdmin.models import Exposition, Display


class ExpoListView(View):

    def get(self, request):
        next_expos_list = Exposition.objects.filter(
            start_date__gte=date.today())

        context = {
            'title': _("Gestion Exposition"),
            'next_expos_list': next_expos_list,
        }
        return render(
            request, 'admin/visualAdmin/display/choose_expo.html', context)


class ExpoManageDisplays(TranslatableModelFormMixin, View):
    form_class = AddDisplayForm
    initial = {'key': 'value'}
    template_name = 'manage_expo.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        self.object = Exposition.objects.get(expo_id=kwargs['exposition'])
        context = {
            'language_tabs': self.get_language_tabs(),
            'form': form
        }
        return render(request, self.template_name, context)
