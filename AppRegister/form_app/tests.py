from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse

from .models import UserProfile


class RegistrationTests(TestCase):
    def valid_data(self, **overrides):
        data = {
            "first_name": "Maria",
            "last_name": "Silva",
            "email": "maria@example.com",
            "phone_number": "(11) 1234-5678",
            "mobile_number": "(11) 91234-5678",
            "address": "Rua Exemplo, 123",
            "cpf": "529.982.247-25",
            "rg": "12.345.678-9",
            "date_of_birth": "1990-05-20",
            "gender": "F",
        }
        data.update(overrides)
        return data

    def test_home_page_renders_form(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cadastro")
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_valid_registration_is_saved_and_redirects(self):
        response = self.client.post(reverse("index"), self.valid_data())
        self.assertRedirects(response, reverse("index"))
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(UserProfile.objects.get().cpf, "52998224725")

    def test_invalid_cpf_is_rejected(self):
        response = self.client.post(reverse("index"), self.valid_data(cpf="111.111.111-11"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CPF inválido.")
        self.assertEqual(UserProfile.objects.count(), 0)

    def test_future_birth_date_is_rejected(self):
        future_date = (date.today() + timedelta(days=1)).isoformat()
        response = self.client.post(reverse("index"), self.valid_data(date_of_birth=future_date, cpf="529.982.247-25"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A data de nascimento não pode estar no futuro.")
        self.assertEqual(UserProfile.objects.count(), 0)

    def test_duplicate_email_is_rejected(self):
        self.client.post(reverse("index"), self.valid_data())
        response = self.client.post(reverse("index"), self.valid_data(
            email="maria@example.com", cpf="111.444.777-35", rg="98.765.432-1"
        ))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserProfile.objects.count(), 1)
