from django.urls import path

from . import views  # ( . ) da pasta que estou import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),  # home
    path('receitas/search/', views.search, name='search'),
    path('receitas/<int:id>/', views.recipe, name="recipe"),  # /recipe
    path('receitas/category/<int:category_id>/',
         views.category, name="category"),

]
