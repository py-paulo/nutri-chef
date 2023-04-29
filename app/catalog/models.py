from django.db import models
from client.models import Client


class TypeFood(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name.capitalize()


class Food(models.Model):
    display_name = models.CharField(max_length=60)
    name = models.CharField(max_length=30)
    type_food = models.ForeignKey(TypeFood, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.display_name


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name[:30]


class ClientNotFood(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    foods = models.ManyToManyField(Food)

    def __str__(self) -> str:
        return self.client.first_name.capitalize()


class FoodRecipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=4000)
    foods = models.ManyToManyField(Food)
    time_prepare = models.IntegerField(default=60)
    food_yield = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class ClientFoodRecipe(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    food_recipe = models.ManyToManyField(FoodRecipe)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.client.first_name.capitalize() + ' ' + self.client.last_name.capitalize()
