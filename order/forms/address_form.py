from django.forms import ModelForm, widgets
from order.models import Address


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['id']
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
        }
