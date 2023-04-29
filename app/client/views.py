from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from .models import Client
from catalog.models import ClientNotFood, FoodRecipe


def index(request):
    clients = Client.objects.order_by("first_name")
    message_error = request.GET.get("error") 
    message_error = message_error.strip().capitalize() if type(message_error) == str else None
    return render(request, "clients.html", {
        "clients": clients,
        "len": clients.__len__,
        "iserror": "yes" if message_error else "no",
        "message_error": message_error
        })


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


def add_food_restriction(request):
    if request.method == "GET":
        return redirect("/clients/?error=invalid method GET for this route!")

    client_id = request.POST.get("client-id")

    return redirect("/clients" + ("/" + client_id if client_id else "/"), success="yes")
