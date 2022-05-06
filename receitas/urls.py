from django.urls import path

from receitas.views import contato, home, sobre

urlpatterns = [
    path('', home),  # home
    path('sobre/', sobre),  # /sobre
    path('contato/', contato),  # /contato
]
