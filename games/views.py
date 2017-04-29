from django.shortcuts import render
from django.http import HttpResponse
from purchase.models import PurchaseRecord
from member.models import Member
from tags.models import Tag
from .models import Game
from reviews.models import Review
from django.contrib.auth.decorators import login_required

def game(request, gameID):
    
    game = Game.objects.get(pk=gameID)
    items = game.items.all()
    bought = []
    bought_any = False
    
    if request.user.is_authenticated():
        member = request.user.member
        for item in items:
            if PurchaseRecord.objects.filter(member=member, item=item):
                bought.append(True)
                bought_any = True
            else:
                bought.append(False)
    else:
        for item in items:
            bought.append(False)

    records = zip(bought, items)
    tags = Tag.objects.get_tags_of_game(game)
    tags = reversed(list(tags))
    reviews = Review.objects.get_reviews_of_game(game)
    context = {'game': game, 'records': records, 'bought':bought_any, 'tags':tags, 'reviews':reviews}
    return render(request, 'games/game.html', context)

def genres(request):
    genres = [choice[1].lower() for choice in Game._meta.get_field('genre').choices]
    context = {'genres': genres}
    return render(request, 'games/genres.html', context)

def genre(request, genre):
    games = Game.objects.filter(genre=genre[:2].upper()).order_by('-date_published')
    context = {'genre': genre, 'games': games}
    return render(request, 'games/genre.html', context)

def tag(request, gameID):
        return HttpResponse("Tags of game #" + gameID)

def add_tag(request, gameID):
        return HttpResponse("Adding tags to game #" + gameID)
        
@login_required
def purchased(request):
    member = request.user.member
    PurchaseRecords = member.get_purchase_history().all()
    games = []
    for record in PurchaseRecords:
        if record.item.game not in games:
            games.append(record.item.game)
    context = {'games': games, 'len': len(games)}
    return render(request, 'member/purchased.html', context)

