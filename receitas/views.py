
from django.shortcuts import render


def home(request):
    # rendezira o arquivo home.html
    return render(request, 'receitas/pages/home.html', context={
        'name': 'Caio Macambira'
    })


def recipe(request, id):
    # rendezira o arquivo home.html
    return render(request, 'receitas/pages/recipe-view.html', context={
        'name': 'Caio Macambira'
    })
