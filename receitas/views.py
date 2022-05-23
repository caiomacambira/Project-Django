

from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.recipes.factory import make_recipe

from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    # rendezira o arquivo home.html
    return render(request, 'receitas/pages/home.html', context={
        # list comprehension de 10 receitas
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id,
                              is_published=True,).order_by('-id'))

    return render(request, 'receitas/pages/category.html', context={
        # list comprehension de 10 receitas
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |',
    })


def recipe(request, id):
    # rendezira o arquivo home.html
    '''recipe = Recipe.objects.filter(
        pk=id, is_published=True,).order_by('-id').first'''

    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

    return render(request, 'receitas/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,  # Se detail page não for True - mostre o botão
    })
