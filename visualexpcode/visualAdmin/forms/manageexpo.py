from django import forms
from django.contrib import admin
admin.autodiscover()
from django.utils.translation import ugettext as _
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from visualAdmin.models import Display, Artwork, Exposition
from django.core.exceptions import ValidationError


class AddDisplayForm(forms.ModelForm):
    artwork = forms.ModelChoiceField(Artwork.objects.all(), widget=ForeignKeyRawIdWidget(Display._meta.get_field('artwork').rel, admin.site)
    )

    def __init__(self,*args,**kwargs):
        self.choice_list = kwargs.pop('choices')
        self.exposition = kwargs.pop('exposition')
        super(AddDisplayForm,self).__init__(*args,**kwargs)
        self.fields['position'].widget = forms.Select(choices=self.choice_list)

    def is_valid(self):
        valid = super(AddDisplayForm, self).is_valid()

        # we're done now if not valid
        if not valid:
            return valid

        current_display_list = Display.objects.filter(exposition__expo_id=self.exposition.expo_id)

        for display in current_display_list:
            if self.cleaned_data['artwork'].artwork_id == display.artwork.artwork_id:
                valid = False
                self._errors['artwork'] = ValidationError(_("Cette oeuvre est déja exposée dans cette exposition"))
                break
            if self.cleaned_data['position'] == display.position:
                valid = False
                self._errors['position'] = ValidationError(_("Cet emplacement est déja pris dans cette exposition"))
                break



        return valid
    class Meta:
        model = Display
        fields = ['artwork', 'position', 'has_arrived']

