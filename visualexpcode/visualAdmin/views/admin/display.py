# from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.views.generic import View
from parler.views import TranslatableModelFormMixin
from visualAdmin.forms.manageexpo import AddDisplayForm
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from datetime import date

from visualAdmin.models import Exposition, Display, Artwork


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
    choice_list = ()
    form_class = AddDisplayForm(choices=choice_list, exposition=None)
    initial = {'key': 'value'}
    template_name = 'manage_expo.html'


    def get(self, request, *args, **kwargs):
        exposition = Exposition.objects.get(expo_id=kwargs['exposition'])
        choice_list= self.get_choice_list(exposition)
        display_list = Display.objects.order_by('position').filter(exposition=exposition)
        form = AddDisplayForm(initial=self.initial, choices=choice_list, exposition=exposition)
        context = {
            'form': form, 
            'exposition' : exposition,
            'display_list' : display_list,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        exposition = Exposition.objects.get(expo_id=kwargs['exposition'])
        choice_list= self.get_choice_list(exposition)
        display_list = Display.objects.order_by('position').filter(exposition=exposition)
        self.initial['exposition'] = exposition.expo_id
        form = AddDisplayForm(request.POST, choices=choice_list, exposition=exposition)
        context = {
            'form': form,
            'exposition' : exposition,
            'display_list' : display_list,
        }
        if form.is_valid():

            new_display = Display.objects.create(artwork_id=form.cleaned_data['artwork'].artwork_id, exposition=exposition, position=form.cleaned_data['position'], has_arrived=form.cleaned_data['has_arrived'])
            new_display.save()

            context['form'] = AddDisplayForm(initial=self.initial, choices=choice_list, exposition=exposition) 
            return render(request, self.template_name, context)

        return render(request, self.template_name, context)

    def get_choice_list(self, exposition):
        displays = exposition.display_set.order_by('position')
        choice_list = ()
        cpt = 1
        for cpt in range(1, 17):
            for display in displays:
                if display.position == cpt:
                    break
            else:
                choice_list = choice_list + ((cpt, str(cpt)),)
        return choice_list

class DisplayDeleteView(DeleteView):
    model = Display
    template_name = 'display_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('manage-expo', kwargs={'exposition': self.kwargs['exposition']})