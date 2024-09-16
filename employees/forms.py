from django import forms
from .models import Employees


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = [
            "name",
            "address",
            "phone_no",
            "salary",
            "designation",
            "short_description",
            "profile_picture",
        ]


class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = [
            "name",
            "address",
            "phone_no",
            "salary",
            "designation",
            "short_description",
        ]

        widgets = {
            'salary': forms.TextInput(attrs={'readonly': True}),
            'designation': forms.TextInput(attrs={'readonly': True}),
        }



