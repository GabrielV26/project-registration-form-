# Formulário de cadastro

Aplicação de cadastro desenvolvida com Django e Bootstrap. O formulário valida os campos e armazena os registros em SQLite durante o desenvolvimento.

## Requisitos

- Python 3.10 ou superior
- pip

## Executar localmente

A partir da raiz do repositório:

```bash
cd AppRegister
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
export DJANGO_DEBUG=true
export DJANGO_SECRET_KEY="chave-local-apenas-para-desenvolvimento"
python manage.py migrate
python manage.py runserver
```

No Windows, ative o ambiente com `.venv\\Scripts\\activate` e defina as variáveis de ambiente no terminal antes de executar os comandos Django.

Acesse http://127.0.0.1:8000/.

## Configuração

- `DJANGO_SECRET_KEY`: obrigatório quando `DJANGO_DEBUG=false`; use uma chave forte e secreta.
- `DJANGO_DEBUG`: mantenha desativado em produção.
- `DJANGO_ALLOWED_HOSTS`: hosts permitidos separados por vírgula.
- `DJANGO_SESSION_COOKIE_SECURE` e `DJANGO_CSRF_COOKIE_SECURE`: habilitados por padrão em produção; precisam ser compatíveis com HTTPS.
- `DJANGO_SECURE_SSL_REDIRECT`: habilite apenas depois de configurar HTTPS corretamente.
- `DJANGO_SECURE_HSTS_SECONDS`: configure apenas depois de confirmar que o domínio inteiro funciona com HTTPS.

Não use a chave de desenvolvimento em produção. Como o formulário trata dados pessoais, restrinja o acesso ao banco e aos registros, evite registrar CPFs/RGs em logs e defina regras de retenção apropriadas.

## Banco de dados

As migrações são versionadas em `form_app/migrations/`. Para aplicar alterações no banco:

```bash
python manage.py migrate
python manage.py makemigrations --check --dry-run
```

## Testes

```bash
python manage.py test
python manage.py check
```
