from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from games.models import Game
from member.models import Member
from .models import Review


def add(request: HttpRequest, game_id: int) -> HttpResponse:
    game = Game.objects.get(pk=game_id)
    member = request.user.member
    content = request.GET.get('content')
    review = Review.create(content, game, member)
    review.save()
    return redirect('games:game', gameID=game_id)
