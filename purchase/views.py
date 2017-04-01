from django.shortcuts import render
from django.http import HttpResponse
from games.models import Item
from .classes import Purchase, Payment
from .models import PurchaseRecord
from member.models import Member, PaymentMethod

# Create your views here.

def purchase(request, game_product_id):
    game_product = Item.objects.get(pk=game_product_id)
    member = Member.objects.get(pk=1)
    member_name = member.nickname
    purchase = Purchase(member, game_product)
    context = {'member':member_name, 'game_product': str(game_product), 'game_product_id':game_product_id, 'reward_count':min(member.get_rewards(), 10)}
    return render(request, 'purchase/purchase.html', context)

def pay(request, game_product_id):
    rewards_to_use = int(request.GET.get('rewards_to_use'))
    game_product = Item.objects.get(pk=game_product_id)
    member = Member.objects.get(pk=1)
    payment_method = member.payment_method
    payment = Payment(payment_method)
    amount = float(game_product.price) * (1 - 0.1 * int(rewards_to_use))
    successful = payment.pay(amount)
    if successful:
        member.use_rewards(rewards_to_use)
        member.accumulate_spending(amount)
        purchase_record = PurchaseRecord.create(member, game_product)
        purchase_record.save()
    context = {'successful':successful, 'amount':round(amount, 2), 'game_product':str(game_product), 'game':game_product.game.pk}
    return render(request, 'purchase/pay.html', context)
