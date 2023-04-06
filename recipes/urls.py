from django.urls import path
from recipes.views import recipe_list, show_recipe

urlpatterns = [
    path("recipes/", recipe_list, name="recipe_list"),
    path("recipes/<int:id>/", show_recipe, name="show_recipe"),
]
