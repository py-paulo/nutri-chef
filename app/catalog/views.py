from django.shortcuts import render
from .models import FoodRecipe


def index(request):
    catalog = list(map(lambda recipe: {
        'name': recipe.name,
        'subject': recipe.subject,
        'description': recipe.description,
        'foods': recipe.foods,
        'time_prepare': recipe.time_prepare,
        'food_yield': recipe.food_yield,
        'ingredients': recipe.ingredients.all()
    }, FoodRecipe.objects.order_by("name")))
    return render(request, "catalog.html", { "catalog": catalog})
