from django.db import models
from client.models import Client


class TypeFood(models.Model):
    name = models.CharField(max_length=50)
  

class Food(models.Model):
    display_name = models.CharField(max_length=60)
    name = models.CharField(max_length=30)
    type_food = models.ForeignKey(TypeFood, on_delete=models.CASCADE)


class FoodRecipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=4000)
    foods = models.ManyToManyField(Food)


class ClientFoodRecipe(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    food_recipe = models.ForeignKey(FoodRecipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
