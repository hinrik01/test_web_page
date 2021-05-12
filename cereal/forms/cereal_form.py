from django.forms import ModelForm, widgets
from django import forms
from cereal.models import Cereal

class CerealUpdateForm(ModelForm):
    class Meta:
        model = Cereal
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'category': widgets.Select(attrs={ 'class': 'form-control' }),
            'price': widgets.NumberInput(attrs={'class': 'form-control' })
        }

class CerealCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    class Meta:
        model = Cereal
        exclude = [ 'id' ]
        widgets = {
            'name': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'description': widgets.TextInput(attrs={ 'class': 'form-control' }),
            'category': widgets.Select(attrs={ 'class': 'form-control' }),
            'price': widgets.NumberInput(attrs={'class': 'form-control' })
        }