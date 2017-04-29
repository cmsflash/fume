from django.shortcuts import render, redirect
from .models import TagItem, Tag
from django.http import HttpResponse
from games.models import Game
from member.models import Member

def tag(request, game_id):
    game = Game.objects.get(pk=game_id)
    member = request.user.member
    tag_items = game.tag_items.all()
    tags = Tag.objects.get_tags_of_game(game)
    context = {'member':member, 'game':game, 'tags':tags}
    return render(request, 'tags/tag.html', context)

def add(request, game_id):
    game = Game.objects.get(pk=game_id)
    member = request.user.member
    label = request.GET.get('tag')
    tag = Tag.objects.get_or_create(label=label)[0]
    tag_item = TagItem.create(tag, member, game)
    tag_item.save()
    return redirect('games:game', gameID=game_id)

def view_games_by_tag(request, label):
    tag = Tag.objects.get(label=label)
    games = Tag.objects.get_games_by_tag(tag)
    context = {'games': games}
    return render(request, 'tags/view_games_by_tag.html', context)

def view_all_tags(request):
    tags = Tag.objects.all()
    context = {'tags':tags}
    return render(request, 'tags/tags.html', context)
