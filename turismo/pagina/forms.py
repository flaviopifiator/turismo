from django import forms
from . import models


class FeedBackFormCliente(forms.ModelForm):
    class Meta:
        model = models.FeedBack
        exclude = ('tipo', 'capacitacion')

    valoracion = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])


class FeedBackFormProveedor(forms.ModelForm):
    class Meta:
        model = models.FeedBack
        exclude = ('tipo', 'proveedor')

    valoracion = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])