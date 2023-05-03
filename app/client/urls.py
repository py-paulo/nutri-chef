from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="clients"),
    path("<int:client_id>/", views.client, name="client"),
    path("add-food-restriction/", views.add_food_restriction, name="add-food-restriction"),
    path("delete-food-restriction/", views.delete_food_restriction, name="delete-food-restriction")
]
