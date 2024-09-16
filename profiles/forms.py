from django import forms
from .models import Profiles

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['bg_image', 'profile_image']