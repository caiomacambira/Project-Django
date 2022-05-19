from django.urls import path

from . import views  # ( . ) da pasta que estou import views

urlpatterns = [
    path('', views.home),  # home
    path('receitas/<int:id>/', views.recipe),  # /recipe
]
