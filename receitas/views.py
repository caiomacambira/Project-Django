

from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):
    # rendezira o arquivo home.html
    return render(request, 'receitas/pages/home.html', context={
        # list comprehension de 10 receitas
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    # rendezira o arquivo home.html
    return render(request, 'receitas/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,  # Se detail page não for True - mostre o botão
    })
