from django.shortcuts import render
from django.http import HttpResponse
from games.models import Item
from .classes import Purchase

# Create your views here.

def purchase(request, game_product_id):
    game_product = Item.objects.get(pk=game_product_id)
    member = 0
    purchase = Purchase(member, game_product)
    return HttpResponse("Buying game product #" + str(game_product))
