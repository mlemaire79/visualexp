from parler import forms
from visualAdmin.models import Display


class AddDisplayForm(forms.TranslatableModelForm):
    class Meta:
        model = Display
        fields = ['artwork', 'delivery_time', 'description']
