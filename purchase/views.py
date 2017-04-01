from django.shortcuts import render
from django.http import HttpResponse
from games.models import Item
from .classes import Purchase
from member.models import Member, PaymentMethod

# Create your views here.

def purchase(request, game_product_id):
    game_product = Item.objects.get(pk=game_product_id)
    member = Member.objects.get(pk=1)
    '''if not members:
        payment_method = PaymentMethod.create(0)
        payment_method.save()
        member = Member.create('qomo_inc', 'samsondai', 'Qomo', 'samson@qomo.com', payment_method)
        member.save()
    else:
        member = members[0]'''
    member_name = member.nickname
    purchase = Purchase(member, game_product)
    context = {'member':member_name, 'game_product': str(game_product), 'game_product_id':game_product_id, 'reward_count':min(member.get_rewards(), 10)}
    return render(request, 'purchase/purchase.html', context)

def pay(request, game_product_id, rewards_to_use):
    game_product = Item.objects.get(pk=game_product_id)
    member = Member.objects.get(pk=1)
    #payment_method = member.paymentmethod
    return HttpResponse('Paying')
    
