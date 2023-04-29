from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="clients"),
    path("<int:client_id>/", views.client, name="client")
]
