from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from catalog.models import ClientNotFood, FoodRecipe, Food

from .models import Client


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


def delete_food_restriction(request):
    if request.method == "GET":
        return redirect("/clients/?error=invalid method GET for this route!")

    client_id = request.POST.get("client-to-delete-food")
    food_name = request.POST.get("delete-food-name")

    if client_id is None:
        return redirect("/clients/?error=Client not found!")

    if food_name is None:
        return redirect("/clients/?error=Food name not found!")

    try:
        food = Food.objects.get(name=food_name.lower())
    except ObjectDoesNotExist:
        return redirect("/clients/?error=food not exists!")

    try:
        client_not_foods = ClientNotFood.objects.get(client=client_id)
        client_not_foods.foods.remove(food)
        client_not_foods.save()
    except ObjectDoesNotExist:
        pass

    return redirect("/clients" + ("/" + client_id if client_id else "/"), success="yes")


def add_food_restriction(request):
    if request.method == "GET":
        return redirect("/clients/?error=invalid method GET for this route!")

    client_id = request.POST.get("client-id")
    food_name = request.POST.get("food-name")

    if client_id is None:
        return redirect("/clients/?error=Client not found!")

    if food_name is None:
        return redirect("/clients/?error=Food name not found!")

    try:
        client_id = int(client_id)
    except ValueError:
        return redirect("/clients/?error=Client not found!")

    try:
        food = Food.objects.get(name=food_name.lower())
    except ObjectDoesNotExist:
        food = Food.objects.create(display_name=food_name.capitalize().strip(), name=food_name.lower().strip())
        food.save()

    client = Client.objects.get(pk=client_id)
    client_not_foods = ClientNotFood.objects.filter(client=client)
    if len(client_not_foods) > 0:
        client_not_foods = client_not_foods[0]
        client_not_foods.foods.add(food)
        client_not_foods.save()
    else:
        client_not_foods = ClientNotFood.objects.create(client=client)
        client_not_foods.foods.add(food)
        client_not_foods.save()

    return redirect("/clients/" + str(client_id), success="yes")
