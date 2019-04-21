from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Review
from games.models import Game
from member.models import Member


def add(request, game_id):
    game = Game.objects.get(pk=game_id)
    member = request.user.member
    content = request.GET.get('content')
    review = Review.create(content, game, member)
    review.save()
    return redirect('games:game', gameID=game_id)
