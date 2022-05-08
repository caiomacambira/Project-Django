
from django.shortcuts import render


def home(request):
    # rendezira o arquivo home.html
    return render(request, 'receitas/home.html', context={
        'name': 'Caio Macambira'
    })
