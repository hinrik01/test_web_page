from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets

from django import forms
from user.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'address']
        widgets = {
            'favorite-candy': widgets.Select(attrs={'class':'form-control'}),
            'profile-image': widgets.TextInput(attrs={'class':'form-control'}),
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
