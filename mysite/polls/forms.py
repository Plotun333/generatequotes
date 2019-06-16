from django import forms
from .models import BEST

class Lookfor(forms.Form):
    quote_name = forms.CharField(label='Quote name', max_length=100)


class MarkerForm(forms.ModelForm):
    class Meta:
        model = BEST
        fields = "__all__"