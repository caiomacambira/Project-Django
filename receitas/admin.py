from django.contrib import admin

from .models import Category, Recipe

# Duas maneiras de registrar models

# Opção 2


class CategoryAdmin(admin.ModelAdmin):
    ...

# Opção 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


# Opção 2
admin.site.register(Category, CategoryAdmin)
