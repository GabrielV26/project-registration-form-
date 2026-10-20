# Generated for the initial UserProfile schema.
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=150, verbose_name="Nome")),
                ("last_name", models.CharField(max_length=150, verbose_name="Sobrenome")),
                ("email", models.EmailField(max_length=254, unique=True, verbose_name="E-mail")),
                ("phone_number", models.CharField(blank=True, max_length=15, null=True, verbose_name="Telefone")),
                ("mobile_number", models.CharField(blank=True, max_length=15, null=True, verbose_name="Celular")),
                ("address", models.TextField(blank=True, null=True, verbose_name="Endereço")),
                ("cpf", models.CharField(max_length=14, unique=True, verbose_name="CPF")),
                ("rg", models.CharField(max_length=12, unique=True, verbose_name="RG")),
                ("date_of_birth", models.DateField(verbose_name="Data de nascimento")),
                ("gender", models.CharField(blank=True, choices=[("M", "Masculino"), ("F", "Feminino")], max_length=10, null=True, verbose_name="Gênero")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
