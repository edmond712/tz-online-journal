from datetime import timedelta
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class DishType(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.PROTECT)
    cooking_time = models.DurationField(default=timedelta)
    category = models.CharField(
        choices=(
            ('breakfast', 'Завтрак'),
            ('lunch', 'Обед'),
            ('diner', 'Ужин'),
        ),
        max_length=10,
        default=1
    )
    dish_type = models.CharField(
        choices=(
            ('salad', 'Салат'),
            ('meat', 'Мясное'),
        ),
        max_length=10,
        default=1
    )
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}. {self.title}'
