from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from games.models import Item, Game
from .classes import Purchase, Payment
from .models import PurchaseRecord
from member.models import Member, PaymentMethod
from datetime import datetime

# Create your views here.

def purchase(request, game_product_id):
    game_product = Item.objects.get(pk=game_product_id)
    if not request.user.is_authenticated():
        return HttpResponse('Please log in or sign up first')
    member = request.user.member
    purchase = Purchase(member, game_product)
    context = {'member':member.nickname, 'game_product': str(game_product), 'game_product_id':game_product_id, 'reward_count':min(member.get_number_of_rewards(), 10)}
    return render(request, 'purchase/purchase.html', context)

def pay(request, game_product_id):
    rewards_to_use = int(request.GET.get('rewards_to_use'))
    item = Item.objects.get(pk=game_product_id)
    if not request.user.is_authenticated():
        return HttpResponse('Please log in or sign up first')
    member = request.user.member
    payment_method = member.payment_method
    payment = Payment(payment_method)
    amount = float(item.price) * (1 - 0.1 * int(rewards_to_use))
    successful = payment.pay(amount)
    if successful:
        member.use_rewards(rewards_to_use)
        member.accumulate_spending(amount)
        purchase_record = PurchaseRecord.create(member, item, datetime.now())
        purchase_record.save()
    context = {'successful':successful, 'amount':round(amount, 2), 'game_product':str(item), 'game':item.game.pk}
    return render(request, 'purchase/pay.html', context)

def clear(request, game_id):
    game = Game.objects.get(pk=game_id)
    items = game.items.all()
    for item in items:
        item.purchase_records.all().delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
