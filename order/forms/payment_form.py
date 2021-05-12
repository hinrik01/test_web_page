from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime

MONTH_CHOICES =(
    ("1", "01"),
    ("2", "02"),
    ("3", "03"),
    ("4", "04"),
    ("5", "05"),
    ("6", "06"),
    ("7", "07"),
    ("8", "08"),
    ("9", "09"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12")
)

YEAR_CHOICES =(
    ("1", "2021"),
    ("2", "2022"),
    ("3", "2023"),
    ("4", "2024"),
    ("5", "2025"),
    ("6", "2026"),
    ("7", "2027"),
    ("8", "2028"),
    ("9", "2029"),
    ("10", "2030")
)


def validate_card_number(card_number):
    if len(str(card_number)) != 12:
        raise ValidationError('Card number not valid')


class PaymentForm(forms.Form):
    cardholder_name = forms.CharField(max_length=100)
    card_number = forms.IntegerField()
    expiration_month = forms.ChoiceField(choices=MONTH_CHOICES)
    expiration_year = forms.ChoiceField(choices=YEAR_CHOICES)
    csv = forms.IntegerField()

    def clean_card_number(self):
        card_number = self.cleaned_data["card_number"]
        if len(str(card_number)) != 16:
            raise ValidationError('Card number needs to of length 16')

        return card_number

    def clean_csv(self):
        csv = self.cleaned_data["csv"]
        if len(str(csv)) != 3:
            raise ValidationError('CSV needs to be of length 3')

        return csv

    def clean(self):
        datetime_now = datetime.today()
        exp_month = self.cleaned_data["expiration_month"]
        exp_year = self.cleaned_data["expiration_year"]
        if (2020 + int(exp_year)) <= datetime_now.year and int(exp_month) < datetime_now.month:
            self.add_error('expiration_month', "Card is expired")









