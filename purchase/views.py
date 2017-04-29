from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from games.models import Item, Game
from .classes import Purchase, Payment
from .models import PurchaseRecord
from member.models import Member, PaymentMethod
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def purchase(request, game_product_id):
    game_product = Item.objects.get(pk=game_product_id)
    member = request.user.member
    purchase = Purchase(member, game_product)
    context = {'member':member.nickname, 'game_product': str(game_product), 'game_product_id':game_product_id, 'reward_count':min(member.get_number_of_rewards(), 10)}
    return render(request, 'purchase/purchase.html', context)

@login_required
def pay(request, game_product_id):
    rewards_to_use = int(request.GET.get('rewards_to_use'))
    item = Item.objects.get(pk=game_product_id)
    member = request.user.member
    purchase = Purchase(member, item)
    purchase.set_number_of_rewards(rewards_to_use)
    successful = purchase.make_payment()
    context = {'successful':successful, 'amount':round(purchase.get_amount(), 2), 'game_product':str(item), 'game':item.game.pk}
    return render(request, 'purchase/pay.html', context)

@login_required
def clear(request, game_id):
    member = request.user.member
    game = Game.objects.get(pk=game_id)
    items = game.items.all()
    for item in items:
        item.purchase_records.filter(member=member).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
