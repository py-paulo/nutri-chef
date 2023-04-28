from django.contrib import admin
from .models import TypeFood, Food, FoodRecipe, ClientFoodRecipe, Ingredient


@admin.register(TypeFood)
class TypeFoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodRecipe)
class FoodRecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientFoodRecipe)
class ClientFoodRecipeAdmin(admin.ModelAdmin):
    pass
