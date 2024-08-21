from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserProfileForm


def index(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formulário enviado com sucesso!')
            # Limpa o formulário
            form = UserProfileForm()
            return redirect('index')  # Redireciona para a página inicial
    else:
        form = UserProfileForm()

    return render(request, 'index.html', {'form': form})
