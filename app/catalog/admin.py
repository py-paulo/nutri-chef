from django.contrib import admin
from .models import Food, FoodRecipe, Ingredient, ClientNotFood


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(ClientNotFood)
class ClientNotFoodAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodRecipe)
class FoodRecipeAdmin(admin.ModelAdmin):
    pass
