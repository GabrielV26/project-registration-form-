from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from validate_docbr import CPF

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "first_name", "last_name", "email", "phone_number",
            "mobile_number", "address", "cpf", "rg", "date_of_birth", "gender",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "autocomplete": "given-name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "autocomplete": "family-name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "exemplo@dominio.com", "autocomplete": "email"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control", "id": "phone", "placeholder": "(XX) XXXX-XXXX", "autocomplete": "tel"}),
            "mobile_number": forms.TextInput(attrs={"class": "form-control", "id": "mobile", "placeholder": "(XX) XXXXX-XXXX", "autocomplete": "tel"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Endereço completo", "autocomplete": "street-address"}),
            "cpf": forms.TextInput(attrs={"class": "form-control", "id": "cpf", "placeholder": "XXX.XXX.XXX-XX", "inputmode": "numeric"}),
            "rg": forms.TextInput(attrs={"class": "form-control", "id": "rg"}),
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control", "autocomplete": "bday"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
        }

    def clean_cpf(self):
        value = self.cleaned_data.get("cpf", "")
        cpf_digits = "".join(char for char in value if char.isdigit())
        if not CPF().validate(cpf_digits):
            raise ValidationError("CPF inválido.")
        return cpf_digits

    def clean_date_of_birth(self):
        value = self.cleaned_data["date_of_birth"]
        if value > date.today():
            raise ValidationError("A data de nascimento não pode estar no futuro.")
        return value
