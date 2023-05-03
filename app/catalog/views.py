from django.shortcuts import render
from .models import FoodRecipe


def index(request):
    catalog = list(map(lambda recipe: {
        'id': recipe.id,
        'name': recipe.name,
        'subject': recipe.subject,
        'description': recipe.description,
        'foods': recipe.foods,
        'time_prepare': recipe.time_prepare,
        'food_yield': recipe.food_yield,
        'ingredients': recipe.ingredients.all()[:5]
    }, FoodRecipe.objects.order_by("name")))
    return render(request, "catalog.html", { "catalog": catalog, "len": catalog.__len__()})


def recipe(request, recipe_id=1):
    recipe = FoodRecipe.objects.get(pk=recipe_id)
    return render(request, "recipe.html", {
        "recipe": recipe,
        "ingredients": recipe.ingredients.all(),
        "title": recipe.name[:15].capitalize() + ('...' if len(recipe.name) > 15 else '')
    })
