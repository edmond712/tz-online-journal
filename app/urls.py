from django.urls import path
from .views import create_recipe, update_recipe, delete_recipe, view_recipe, recipe_list

urlpatterns = [
    path('recipes/', recipe_list),
    path('recipes/create/', create_recipe),
    path('recipes/<int:recipe_id>/', view_recipe),
    path('recipes/<int:recipe_id>/delete/', delete_recipe),
    path('recipes/<int:recipe_id>/update/', update_recipe),
]
