from django.shortcuts import render
from django.http import HttpResponse
from purchase.models import PurchaseRecord
from member.models import Member
from tags.models import Tag
from .models import Game

def game(request, gameID):
    game = Game.objects.get(pk=gameID)
    if not request.user.is_authenticated():
        return HttpResponse('Please log in or sign up first')
    member = request.user.member
    items = game.items.all()
    bought = []
    bought_any = False
    for item in items:
        if PurchaseRecord.objects.filter(member=member, item=item):
            bought.append(True)
            bought_any = True
        else:
            bought.append(False)
    records = zip(bought, items)
    tags = Tag.objects.get_tags_of_game(game)
    tags = reversed(list(tags))
    context = {'game': game, 'records': records, 'bought':bought_any, 'tags':tags}
    return render(request, 'games/game.html', context)

def genres(request):
    genres = [choice[1].lower() for choice in Game._meta.get_field('genre').choices]
    context = {'genres': genres}
    return render(request, 'games/genres.html', context)

def genre(request, genre):
    games = Game.objects.filter(genre=genre[:2].upper())
    context = {'genre': genre, 'games': games}
    return render(request, 'games/genre.html', context)

def tag(request, gameID):
        return HttpResponse("Tags of game #" + gameID)

def add_tag(request, gameID):
        return HttpResponse("Adding tags to game #" + gameID)
