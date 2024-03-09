import django.contrib.admin
from django.contrib import admin
from .models import Recipe, Ingredients, User, DishType, Category

admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(User)
admin.site.register(DishType)
admin.site.register(Category)
