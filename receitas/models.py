from email.policy import default
from unicodedata import category

from django.contrib.auth.models import User
from django.db import models

#charfield - varchar
# slugfield - geralmente são usados ​​em URLs
#integerfield - int
#booleanfield - boolean
# Textfield - text area(input),sem limite
# Datetimefield(auto_now_add) - no momento da criação gerar uma data
# Datetimefield(auto_now) - é chamado quando o registro for atualizado
# ImageField(upload_to= '') - recebe um upload
# SET_NULL - caso a categoria for apagada,os campos da categoria setem a cateoria como valor NULO


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):  # chama o model como uma string
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title
# Campos do banco de dados:

# title description slug
# preparation_time preparation_time_unit
# servings servings_unit
# preparation_step
# preparation_step_is_html
# created_at updated_at
# is_published
# cover
# category (Relação)
# Author (Relação)
