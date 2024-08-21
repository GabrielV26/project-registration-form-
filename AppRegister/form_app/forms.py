from django import forms
from .models import UserProfile
from validate_docbr import CPF
from django.core.exceptions import ValidationError


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'mobile_number', 'address', 'cpf', 'rg', 'date_of_birth', 'gender']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'exemplo@dominio.com'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'phone',
                'placeholder': '(XX) XXXX-XXXX'
            }),
            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'mobile',
                'placeholder': '(XX) XXXXX-XXXX'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Endereço completo'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'id':  "cpf",
                'placeholder': 'XXX.XXX.XXX-XX'
            }),
            'rg': forms.TextInput(attrs={
                'class': 'form-control',
                'id':  "rg",
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

    def clean_cpf(self):
        cpf_input = self.cleaned_data.get('cpf')
        cpf = CPF()

        # Validar o CPF
        if not cpf.validate(cpf_input):
            raise ValidationError("CPF inválido.")

        return cpf_input
