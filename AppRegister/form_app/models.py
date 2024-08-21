from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Nome')
    last_name = models.CharField(max_length=150, verbose_name='Sobrenome')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefone')
    mobile_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Celular')
    address = models.TextField(blank=True, null=True, verbose_name='Endereço')
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    rg = models.CharField(max_length=12, unique=True, verbose_name='RG')
    date_of_birth = models.DateField(verbose_name='Data de nascimento')
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')], blank=True, null=True, verbose_name='Gênero')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

