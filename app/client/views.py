from django.shortcuts import render
from .models import Client
from catalog.models import ClientNotFood, FoodRecipe
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    clients = Client.objects.order_by("first_name")
    return render(request, "clients.html", { "clients": clients, "len": clients.__len__ } )


def client(request, client_id=1):
    client = Client.objects.get(pk=client_id)
    try:
        not_foods = ClientNotFood.objects.get(client=client).foods.all()
    except ObjectDoesNotExist:
        not_foods = []
    catalog = list(
        filter(lambda recipe: not any(item in recipe.foods.all() for item in not_foods), FoodRecipe.objects.all())
    )
    catalog = list(map(lambda recipe: {
        'id': recipe.id,
        'name': recipe.name,
        'subject': recipe.subject,
        'description': recipe.description,
        'foods': recipe.foods,
        'time_prepare': recipe.time_prepare,
        'food_yield': recipe.food_yield,
        'ingredients': recipe.ingredients.all()[:5]
    }, catalog))
    return render(request, "client.html", { "client": client, "not_foods": not_foods, "catalog": catalog } )
