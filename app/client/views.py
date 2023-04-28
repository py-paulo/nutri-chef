from django.shortcuts import render
from .models import Client


def index(request):
    clients = Client.objects.order_by("first_name")
    return render(request, "clients.html", { "clients": clients, "len": clients.__len__ } )
